from motor.motor_asyncio import AsyncIOMotorClient
import os
from typing import List, Optional, Dict, Any
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class Database:
    def __init__(self):
        self.client = None
        self.db = None
    
    async def connect(self):
        """Initialize database connection"""
        try:
            mongo_url = os.environ.get('MONGO_URL', 'mongodb://localhost:27017')
            db_name = os.environ.get('DB_NAME', 'hdmonks')
            
            self.client = AsyncIOMotorClient(mongo_url)
            self.db = self.client[db_name]
            
            # Test connection
            await self.client.admin.command('ping')
            logger.info("Connected to MongoDB successfully")
            
        except Exception as e:
            logger.error(f"Failed to connect to MongoDB: {str(e)}")
            raise
    
    async def close(self):
        """Close database connection"""
        if self.client:
            self.client.close()
            logger.info("MongoDB connection closed")
    
    # ===== STAGE OPERATIONS =====
    
    async def get_all_stages(self) -> List[Dict[str, Any]]:
        """Get all stages with their services"""
        if self.db is None:
            await self.connect()
        
        cursor = self.db.stages.find({}, {"_id": 0}).sort("id", 1)
        stages = await cursor.to_list(length=None)
        return stages
    
    async def get_stage_by_id(self, stage_id: int) -> Optional[Dict[str, Any]]:
        """Get a specific stage by ID"""
        if self.db is None:
            await self.connect()
        
        stage = await self.db.stages.find_one({"id": stage_id}, {"_id": 0})
        return stage
    
    async def create_stage(self, stage_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new stage"""
        if self.db is None:
            await self.connect()
        
        # Convert datetime objects to ISO strings for MongoDB
        stage_data = self._serialize_datetime(stage_data)
        
        await self.db.stages.insert_one(stage_data)
        return stage_data
    
    async def update_stage(self, stage_id: int, update_data: Dict[str, Any]) -> bool:
        """Update a stage"""
        if self.db is None:
            await self.connect()
        
        update_data = self._serialize_datetime(update_data)
        
        result = await self.db.stages.update_one(
            {"id": stage_id},
            {"$set": update_data}
        )
        return result.modified_count > 0
    
    async def delete_stage(self, stage_id: int) -> bool:
        """Delete a stage"""
        if self.db is None:
            await self.connect()
        
        result = await self.db.stages.delete_one({"id": stage_id})
        return result.deleted_count > 0
    
    # ===== SERVICE OPERATIONS =====
    
    async def get_service_by_service_id(self, service_id: str) -> Optional[Dict[str, Any]]:
        """Get a service by service_id across all stages"""
        if self.db is None:
            await self.connect()
        
        stage = await self.db.stages.find_one(
            {"services.service_id": service_id},
            {"_id": 0, "services.$": 1}
        )
        
        if stage and "services" in stage and len(stage["services"]) > 0:
            return stage["services"][0]
        return None
    
    async def add_service_to_stage(self, stage_id: int, service_data: Dict[str, Any]) -> bool:
        """Add a service to a stage"""
        if self.db is None:
            await self.connect()
        
        service_data = self._serialize_datetime(service_data)
        
        result = await self.db.stages.update_one(
            {"id": stage_id},
            {"$push": {"services": service_data}}
        )
        return result.modified_count > 0
    
    async def update_service_in_stage(self, stage_id: int, service_id: str, update_data: Dict[str, Any]) -> bool:
        """Update a service within a stage"""
        if self.db is None:
            await self.connect()
        
        update_data = self._serialize_datetime(update_data)
        
        # Create update query for nested service
        update_query = {}
        for key, value in update_data.items():
            update_query[f"services.$.{key}"] = value
        
        result = await self.db.stages.update_one(
            {"id": stage_id, "services.service_id": service_id},
            {"$set": update_query}
        )
        return result.modified_count > 0
    
    async def delete_service_from_stage(self, stage_id: int, service_id: str) -> bool:
        """Delete a service from a stage"""
        if self.db is None:
            await self.connect()
        
        result = await self.db.stages.update_one(
            {"id": stage_id},
            {"$pull": {"services": {"service_id": service_id}}}
        )
        return result.modified_count > 0
    
    # ===== CONTACT INQUIRY OPERATIONS =====
    
    async def create_contact_inquiry(self, inquiry_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new contact inquiry"""
        if self.db is None:
            await self.connect()
        
        inquiry_data = self._serialize_datetime(inquiry_data)
        
        await self.db.contact_inquiries.insert_one(inquiry_data)
        return inquiry_data
    
    async def get_all_inquiries(self, skip: int = 0, limit: int = 100) -> List[Dict[str, Any]]:
        """Get all contact inquiries"""
        if self.db is None:
            await self.connect()
        
        cursor = self.db.contact_inquiries.find({}, {"_id": 0}).sort("created_at", -1).skip(skip).limit(limit)
        inquiries = await cursor.to_list(length=None)
        return inquiries
    
    async def update_inquiry_status(self, inquiry_id: str, status: str) -> bool:
        """Update inquiry status"""
        if self.db is None:
            await self.connect()
        
        result = await self.db.contact_inquiries.update_one(
            {"id": inquiry_id},
            {"$set": {"status": status, "updated_at": datetime.utcnow().isoformat()}}
        )
        return result.modified_count > 0
    
    # ===== TIME SLOT OPERATIONS =====
    
    async def get_available_timeslots(self, date: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get available time slots"""
        if self.db is None:
            await self.connect()
        
        query = {"is_available": True}
        if date:
            query["date"] = date
        
        cursor = self.db.timeslots.find(query, {"_id": 0}).sort([("date", 1), ("time", 1)])
        timeslots = await cursor.to_list(length=None)
        return timeslots
    
    async def get_timeslot_by_id(self, timeslot_id: str) -> Optional[Dict[str, Any]]:
        """Get a timeslot by ID"""
        if self.db is None:
            await self.connect()
        
        timeslot = await self.db.timeslots.find_one({"id": timeslot_id}, {"_id": 0})
        return timeslot
    
    async def create_timeslot(self, timeslot_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new time slot"""
        if self.db is None:
            await self.connect()
        
        timeslot_data = self._serialize_datetime(timeslot_data)
        
        await self.db.timeslots.insert_one(timeslot_data)
        return timeslot_data
    
    async def mark_timeslot_unavailable(self, timeslot_id: str) -> bool:
        """Mark a timeslot as unavailable"""
        if self.db is None:
            await self.connect()
        
        result = await self.db.timeslots.update_one(
            {"id": timeslot_id},
            {"$set": {"is_available": False}}
        )
        return result.modified_count > 0
    
    async def delete_timeslot(self, timeslot_id: str) -> bool:
        """Delete a time slot"""
        if self.db is None:
            await self.connect()
        
        result = await self.db.timeslots.delete_one({"id": timeslot_id})
        return result.deleted_count > 0
    
    # ===== BOOKING OPERATIONS =====
    
    async def create_booking(self, booking_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new consultation booking"""
        if self.db is None:
            await self.connect()
        
        booking_data = self._serialize_datetime(booking_data)
        
        await self.db.bookings.insert_one(booking_data)
        return booking_data
    
    async def get_all_bookings(self, skip: int = 0, limit: int = 100) -> List[Dict[str, Any]]:
        """Get all consultation bookings"""
        if self.db is None:
            await self.connect()
        
        cursor = self.db.bookings.find({}, {"_id": 0}).sort("created_at", -1).skip(skip).limit(limit)
        bookings = await cursor.to_list(length=None)
        return bookings
    
    async def update_booking_status(self, booking_id: str, status: str) -> bool:
        """Update booking status"""
        if self.db is None:
            await self.connect()
        
        result = await self.db.bookings.update_one(
            {"id": booking_id},
            {"$set": {"status": status, "updated_at": datetime.utcnow().isoformat()}}
        )
        return result.modified_count > 0
    
    # ===== UTILITY METHODS =====
    
    def _serialize_datetime(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Convert datetime objects to ISO strings for MongoDB storage"""
        if isinstance(data, dict):
            result = {}
            for key, value in data.items():
                if isinstance(value, datetime):
                    result[key] = value.isoformat()
                elif isinstance(value, dict):
                    result[key] = self._serialize_datetime(value)
                elif isinstance(value, list):
                    result[key] = [self._serialize_datetime(item) if isinstance(item, dict) else item for item in value]
                else:
                    result[key] = value
            return result
        return data


# Global database instance
database = Database()