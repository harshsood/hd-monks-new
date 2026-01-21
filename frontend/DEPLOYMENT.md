# HD Monks Frontend - Vercel Deployment Guide

## Quick Deployment Checklist

✅ **Pre-deployment:**
- [x] Fixed all ESLint warnings
- [x] Fixed React Hook dependencies  
- [x] Added environment variable configuration
- [x] Created `.env.example` for reference
- [x] Added Vercel configuration (`vercel.json`)
- [x] Updated `.gitignore` for deployment safety
- [x] Tested production build locally

## Step-by-Step Deployment Instructions

### 1. Prepare Your Code

Ensure all files are committed to your Git repository:

```bash
git add .
git commit -m "Prepare frontend for Vercel deployment"
git push origin main
```

### 2. Create Vercel Project

1. Go to [https://vercel.com](https://vercel.com)
2. Sign in with your GitHub account
3. Click "Add New..." → "Project"
4. Select your GitHub repository
5. Click "Import"

### 3. Configure Environment Variables

In the Vercel project dashboard:

1. Go to **Settings** → **Environment Variables**
2. Add a new environment variable:
   - **Name:** `REACT_APP_BACKEND_URL`
   - **Value:** Your backend API URL (e.g., `https://api.hdmonks.com`)
   - **Environments:** Select `Production`, `Preview`, and `Development`
3. Click "Save"

### 4. Configure Build Settings

The `vercel.json` file already has the correct configuration, but verify:

- **Build Command:** `npm install --legacy-peer-deps && npm run build`
- **Output Directory:** `build`
- **Install Command:** `npm install --legacy-peer-deps`

### 5. Deploy

Click the "Deploy" button. Vercel will:
1. Clone your repository
2. Install dependencies with `npm install --legacy-peer-deps`
3. Run `npm run build`
4. Deploy the `build` folder to Vercel's CDN

Deployment typically takes 2-3 minutes.

## Post-Deployment

### 1. Test Your Deployment

- Visit your Vercel URL (e.g., `https://your-project.vercel.app`)
- Test navigation between pages
- Test API calls (check browser console for errors)
- Test responsive design on mobile

### 2. Set Up Custom Domain (Optional)

1. Go to **Settings** → **Domains**
2. Add your custom domain
3. Update your DNS records following Vercel's instructions

### 3. Enable Analytics (Optional)

1. Go to **Analytics**
2. Enable Web Analytics to track performance

## Troubleshooting

### Build Fails with "craco: not found"
The `vercel.json` install command includes `npm install --legacy-peer-deps` to handle this.

### API Calls Return 404 or CORS Errors
1. Verify `REACT_APP_BACKEND_URL` is set correctly in Vercel settings
2. Check your backend CORS configuration allows requests from your Vercel domain
3. The Vercel domain format is usually `https://your-project.vercel.app`

### Environment Variables Not Working
1. Redeploy after setting environment variables (Settings → Redeploy)
2. Verify variable names are prefixed with `REACT_APP_` for React app
3. Check variable values don't have extra spaces

### Static Files Return 404
Ensure `build` folder is included and the `vercel.json` route configuration is correct.

## Environment Variables Reference

| Variable | Required | Example |
|----------|----------|---------|
| `REACT_APP_BACKEND_URL` | Yes | `https://api.hdmonks.com` |

## Build Size

- **JavaScript:** ~130 KB (gzipped)
- **CSS:** ~10.7 KB (gzipped)
- **Total:** ~141 KB (gzipped)

## Performance Tips

1. **Enable Caching:** Vercel automatically caches static assets
2. **Monitor Core Web Vitals:** Use Vercel Analytics
3. **Optimize Images:** Use image optimization tools
4. **Enable Edge Functions:** For API rate limiting (advanced)

## Monitoring

Set up monitoring in Vercel:
1. Go to **Settings** → **Monitoring**
2. Enable notifications for deployment failures
3. Check deployment logs regularly

## Rollback Deployment

If something goes wrong:
1. Go to **Deployments**
2. Find the previous successful deployment
3. Click "..." → "Promote to Production"

## Environment-Specific Configuration

### Development
```
REACT_APP_BACKEND_URL=http://localhost:5000
```

### Production
```
REACT_APP_BACKEND_URL=https://api.hdmonks.com
```

Set these in Vercel project settings for each environment.

## CI/CD Configuration

Vercel automatically:
- Builds on every push to main branch
- Creates preview deployments for pull requests
- Provides automatic rollback on deployment failure

## Support & Resources

- [Vercel Documentation](https://vercel.com/docs)
- [Create React App Deployment](https://create-react-app.dev/deployment/)
- [Environment Variables in Vercel](https://vercel.com/docs/concepts/projects/environment-variables)

---

**Last Updated:** January 21, 2026
**Deployment Status:** Ready for Production
