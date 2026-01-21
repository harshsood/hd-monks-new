# Vercel Build Error - Fix

## Problem
Vercel is trying to build from the root directory, but the frontend code is in `/frontend`.

## Solution

You have TWO options:

### Option 1: Set Root Directory in Vercel (RECOMMENDED) ⭐

1. Go to your **Vercel Project**
2. Go to **Settings** → **Root Directory**
3. Change from `.` to `frontend`
4. Click **Save**
5. Redeploy

### Option 2: Update Build Command

In your **Vercel Project Settings** → **Build & Development Settings**:

**Build Command:**
```
cd frontend && npm ci --legacy-peer-deps && npm run build
```

**Install Command:**
```
cd frontend && npm ci --legacy-peer-deps
```

**Output Directory:**
```
frontend/build
```

Then click **Redeploy**.

---

## After Fix

Vercel will now:
1. Navigate to frontend directory
2. Install dependencies with `--legacy-peer-deps`
3. Build the React app
4. Deploy successfully

Try **Option 1** first (it's simpler) - just set the root directory to `frontend` in Vercel settings.
