# 🚀 Complete Deployment Guide - Frontend + Backend

## Overview

This guide walks you through deploying both the HD Monks frontend and backend to production.

### Deployment Stack
- **Frontend**: Vercel (React)
- **Backend**: Render.com (FastAPI)
- **Database**: MongoDB Atlas (Free tier)

---

## ⚡ Quick Timeline

1. **Backend Setup**: 15 minutes
   - Create MongoDB Atlas account
   - Deploy backend to Render.com
   - Get backend URL

2. **Frontend Setup**: 10 minutes
   - Set backend URL in Vercel
   - Redeploy frontend
   - Test connectivity

3. **Total Time**: ~30 minutes

---

## Phase 1: Backend Deployment (15 min)

### Step 1.1: Create MongoDB Atlas Account

Your MongoDB cluster is already created! 

**Connection Details:**
- Cluster: `cluster0.b5sxnrw.mongodb.net`
- Username: `sr4ipr`
- Get your password from MongoDB Atlas dashboard

Connection string:
```
mongodb+srv://sr4ipr:<your_password>@cluster0.b5sxnrw.mongodb.net/?appName=Cluster0
```

### Step 1.2: Deploy Backend to Render.com

1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Click "New +" → "Web Service"
4. Select your GitHub repo (`hd-monks-new`)
5. Configure:
   - **Name**: `hd-monks-api`
   - **Build Command**: `cd backend && pip install -r requirements.txt`
   - **Start Command**: `cd backend && uvicorn server:app --host 0.0.0.0 --port $PORT`

### Step 1.3: Add Environment Variables (in Render Dashboard)

Add these in Settings → Environment:
```
MONGO_URL=mongodb+srv://sr4ipr:<your_password>@cluster0.b5sxnrw.mongodb.net/?appName=Cluster0
DB_NAME=hdmonks
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
JWT_SECRET=your_jwt_secret_key
ENVIRONMENT=production
```

### Step 1.4: Deploy
- Click "Create Web Service"
- Wait 2-3 minutes for build to complete
- Note your URL: `https://hd-monks-api.onrender.com`

### Step 1.5: Test Backend

```bash
curl https://hd-monks-api.onrender.com/api/
```

Should return:
```json
{"message": "HD MONKS API is running", "status": "healthy"}
```

---

## Phase 2: Frontend Deployment (10 min)

### Step 2.1: Update Frontend Environment

In your Vercel project:
1. Go to **Settings** → **Environment Variables**
2. Add/Update:
   - **Name**: `REACT_APP_BACKEND_URL`
   - **Value**: `https://hd-monks-api.onrender.com` (your backend URL)
   - **Environments**: Production, Preview, Development

### Step 2.2: Redeploy Frontend

1. In Vercel, go to **Deployments**
2. Click "..." next to latest deployment
3. Click "Redeploy"
4. Wait for build to complete

Or push a commit:
```bash
git commit --allow-empty -m "Update backend URL"
git push origin main
```

### Step 2.3: Test Frontend

1. Go to your Vercel URL: `https://your-project.vercel.app`
2. Open browser DevTools (F12)
3. Check Console for any errors
4. Navigate pages - should load data from backend

---

## 🧪 Verification Checklist

### Backend
- [ ] Backend URL is accessible: `https://hd-monks-api.onrender.com/api/`
- [ ] Health check returns `{"status": "healthy"}`
- [ ] MongoDB connection successful (check Render logs)
- [ ] Environment variables set in Render

### Frontend
- [ ] Frontend builds successfully on Vercel
- [ ] `REACT_APP_BACKEND_URL` set in Vercel settings
- [ ] No CORS errors in browser console
- [ ] API endpoints return data
- [ ] Pages load and display content

---

## 🐛 Troubleshooting

### Backend Issues

| Problem | Solution |
|---------|----------|
| Build fails | Check Python version 3.9+, requirements.txt present |
| MongoDB connection error | Verify MONGO_URL and add Render IP to MongoDB whitelist |
| Port error | Render auto-assigns PORT, use `$PORT` in command |
| Logs not showing | Check Render dashboard logs tab |

**Add IP to MongoDB:**
1. MongoDB Atlas → Network Access
2. Add IP address: `0.0.0.0/0` (or Render IP)
3. Wait 5 minutes for changes

### Frontend Issues

| Problem | Solution |
|---------|----------|
| API returns 404 | Verify `REACT_APP_BACKEND_URL` in Vercel settings |
| CORS errors | Backend has `allow_origins=["*"]` configured |
| Blank page | Check browser console for errors |
| Build fails locally | Run `npm install --legacy-peer-deps` |

**Debug CORS:**
```javascript
// In browser console
fetch('https://hd-monks-api.onrender.com/api/')
  .then(r => r.json())
  .then(d => console.log(d))
  .catch(e => console.error(e))
```

---

## 📋 Environment Variables Summary

### Backend (`backend/.env` or Render settings)
```env
MONGO_URL=mongodb+srv://sr4ipr:<your_password>@cluster0.b5sxnrw.mongodb.net/?appName=Cluster0
DB_NAME=hdmonks
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
JWT_SECRET=your_jwt_secret_key
ENVIRONMENT=production
```

### Frontend (Vercel settings or `.env`)
```env
REACT_APP_BACKEND_URL=https://hd-monks-api.onrender.com
```

---

## 🚀 Going Live Checklist

- [ ] Backend deployed to Render
- [ ] Backend URL verified working
- [ ] Frontend environment variable set
- [ ] Frontend redeployed
- [ ] API connectivity tested
- [ ] All pages load correctly
- [ ] No console errors
- [ ] Mobile responsive works

---

## 📱 Local Development

### Backend Locally
```bash
cd backend
pip install -r requirements.txt
python main.py
# Runs on http://localhost:8000
```

### Frontend Locally
```bash
cd frontend
npm install --legacy-peer-deps
npm start
# Runs on http://localhost:3000
```

Set `frontend/.env.local`:
```
REACT_APP_BACKEND_URL=http://localhost:8000
```

---

## 🔄 Redeployment

### Update Backend Code
```bash
git add .
git commit -m "Update backend"
git push origin main
# Render auto-deploys from main branch
```

### Update Frontend Code
```bash
git add .
git commit -m "Update frontend"
git push origin main
# Vercel auto-deploys from main branch
```

---

## 💡 Pro Tips

1. **Monitor Render**: Check logs regularly for errors
2. **Test API**: Use curl or Postman to test endpoints
3. **Vercel Analytics**: Enable analytics to track usage
4. **Auto-redeploy**: Both Render and Vercel watch main branch
5. **CORS Issues**: Backend already configured with `allow_origins=["*"]`

---

## 📞 Support

- **Render Docs**: [docs.render.com](https://docs.render.com)
- **Vercel Docs**: [vercel.com/docs](https://vercel.com/docs)
- **MongoDB Docs**: [docs.mongodb.com](https://docs.mongodb.com)
- **FastAPI Docs**: [fastapi.tiangolo.com](https://fastapi.tiangolo.com)

---

**Status**: ✅ Ready for Deployment

**Next Step**: Start with Phase 1 - Backend Deployment
