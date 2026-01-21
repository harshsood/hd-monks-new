from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uuid


# ===== STAGE AND SERVICE MODELS =====

class Service(BaseModel):
    service_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str
    price: Optional[str] = None
    duration: Optional[str] = None
    features: List[str] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ServiceCreate(BaseModel):
    title: str
    description: str
    price: Optional[str] = None
    duration: Optional[str] = None
    features: List[str] = []


class ServiceUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[str] = None
    duration: Optional[str] = None
    features: Optional[List[str]] = None


class Stage(BaseModel):
    id: int
    title: str
    subtitle: str
    phase: str
    services: List[Service] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class StageCreate(BaseModel):
    id: int
    title: str
    subtitle: str
    phase: str
    services: List[ServiceCreate] = []


class StageUpdate(BaseModel):
    title: Optional[str] = None
    subtitle: Optional[str] = None
    phase: Optional[str] = None


# ===== CONTACT INQUIRY MODELS =====

class ContactInquiry(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: str
    phone: Optional[str] = None
    company: Optional[str] = None
    message: str
    service_interest: Optional[str] = None
    status: str = "new"  # new, contacted, qualified, closed
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ContactInquiryCreate(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    company: Optional[str] = None
    message: str
    service_interest: Optional[str] = None


# ===== TIME SLOT AND BOOKING MODELS =====

class TimeSlot(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    date: str  # YYYY-MM-DD format
    time: str  # HH:MM format
    is_available: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)


class TimeSlotCreate(BaseModel):
    date: str
    time: str


class ConsultationBooking(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: str
    phone: str
    company: Optional[str] = None
    service_interest: str
    message: Optional[str] = None
    date: str
    time: str
    timeslot_id: str
    status: str = "confirmed"  # confirmed, completed, cancelled, no_show
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ConsultationBookingCreate(BaseModel):
    name: str
    email: str
    phone: str
    company: Optional[str] = None
    service_interest: str
    message: Optional[str] = None
    timeslot_id: str