# 🔧 Fix Render Deployment Error

## The Problem
Render couldn't find `requirements.txt` because it's looking in the root directory, but the file is in the `/backend` folder.

## The Solution

In your Render.com dashboard, update these settings:

### Build Command
```
cd backend && pip install -r requirements.txt
```

### Start Command  
```
cd backend && uvicorn server:app --host 0.0.0.0 --port $PORT
```

## Steps to Update in Render Dashboard

1. Go to: https://dashboard.render.com/web/srv-d5o5ghd6ubrc73f9v9kg
2. Click **Settings** (left sidebar)
3. Scroll to **Build Command**
   - Replace with: `cd backend && pip install -r requirements.txt`
4. Scroll to **Start Command**
   - Replace with: `cd backend && uvicorn server:app --host 0.0.0.0 --port $PORT`
5. Click **Save Changes**
6. Click **Manual Deploy** → **Deploy latest commit**

---

## ⏳ Wait for Build

The build should now:
1. ✅ Change to backend directory
2. ✅ Find requirements.txt
3. ✅ Install dependencies
4. ✅ Start uvicorn server
5. ✅ Your backend should be live!

---

## ✅ Verify Success

Once deployed, test your backend:
```bash
curl https://hd-monks-api.onrender.com/api/
```

Should return:
```json
{"message": "HD MONKS API is running", "status": "healthy"}
```

If you see this, backend is working! ✅
