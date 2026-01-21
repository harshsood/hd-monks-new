# Backend Service Deployment Guide

## Deploy Backend to Render.com (Recommended)

### Step 1: Prepare Backend

1. **Create `.env` file** in backend directory with:
```env
MONGO_URL=mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority
DB_NAME=hdmonks
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
JWT_SECRET=your_jwt_secret_key
ENVIRONMENT=production
```

### Step 2: Deploy on Render.com

1. Go to [render.com](https://render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Select the `hd-monks-new` repository

#### Configuration:
- **Name**: `hd-monks-api`
- **Runtime**: Python 3
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn server:app --host 0.0.0.0 --port $PORT`
- **Environment**: Production
- **Plan**: Free tier available

#### Environment Variables (Set in Render Dashboard):
```
MONGO_URL=your_mongodb_connection_string
DB_NAME=hdmonks
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
JWT_SECRET=your_jwt_secret
ENVIRONMENT=production
```

### Step 3: Get Your Backend URL

After deployment, your URL will be:
```
https://hd-monks-api.onrender.com
```

### Step 4: Update Frontend

Set frontend environment variable in Vercel:
```
REACT_APP_BACKEND_URL=https://hd-monks-api.onrender.com
```

## Alternative: Deploy on Railway.app

1. Go to [railway.app](https://railway.app)
2. Click "New Project" → "Deploy from GitHub"
3. Select your repository
4. Add environment variables
5. Railway will auto-detect and deploy

---

## Required MongoDB Setup

1. Create free MongoDB Atlas cluster at [mongodb.com/cloud/atlas](https://www.mongodb.com/cloud/atlas)
2. Get connection string: `mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority`
3. Add to backend environment variables

---

## Monitoring

- **Render Dashboard**: View logs and metrics
- **Railway Dashboard**: Real-time monitoring
- **Test API**: `https://your-backend-url/api/` (should return health check)

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| MongoDB Connection Error | Verify MONGO_URL and IP whitelist in MongoDB Atlas |
| CORS Errors | Backend already has `allow_origins=["*"]` |
| Port Already in Use | Use `PORT` environment variable (auto-set by platform) |
| Build Failures | Check requirements.txt is present and Python 3.9+ |

