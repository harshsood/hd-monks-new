# Backend Quick Deploy

## 1 Minute Deploy to Render.com

### Step 1: Prepare
```bash
# Create .env file from template
cp .env.example .env
# Edit .env with your MongoDB and email credentials
```

### Step 2: Deploy
1. Go to https://render.com
2. Click "New +" → "Web Service"
3. Connect GitHub → Select `hd-monks-new`
4. Fill in:
   - **Name**: `hd-monks-api`
   - **Build Command**: `cd backend && pip install -r requirements.txt`
   - **Start Command**: `cd backend && uvicorn server:app --host 0.0.0.0 --port $PORT`

### Step 3: Set Environment Variables (in Render)
```
MONGO_URL=mongodb+srv://sr4ipr:<your_password>@cluster0.b5sxnrw.mongodb.net/?appName=Cluster0
DB_NAME=hdmonks
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
JWT_SECRET=your_jwt_secret_key
ENVIRONMENT=production
```

### Step 4: Deploy & Get URL
After build succeeds (2-3 minutes):
```
Your Backend URL: https://hd-monks-api.onrender.com
```

### Step 5: Update Frontend
In Vercel, set:
```
REACT_APP_BACKEND_URL=https://hd-monks-api.onrender.com
```

---

## ✅ What You Need

- [ ] MongoDB Atlas account (free)
- [ ] Render.com account (free)
- [ ] GitHub repository connected
- [ ] Email credentials for notifications

---

## 🧪 Test

```bash
curl https://hd-monks-api.onrender.com/api/
```

Should return:
```json
{"message": "HD MONKS API is running", "status": "healthy"}
```
