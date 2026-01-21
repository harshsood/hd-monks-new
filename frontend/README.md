# HD Monks Frontend

This is the frontend application for HD Monks, a business consulting platform. Built with React, TailwindCSS, and Shadcn UI components.

## Prerequisites

- Node.js 16+ and npm/yarn
- Backend API running (for API calls)

## Setup Instructions

### 1. Install Dependencies

```bash
npm install --legacy-peer-deps
```

### 2. Environment Variables

Create a `.env.local` file in the frontend directory (see `.env.example`):

```bash
cp .env.example .env.local
```

Update `.env.local` with your backend API URL:

```
REACT_APP_BACKEND_URL=https://your-api-url.com
```

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

## Deployment to Vercel

### Prerequisites
- Vercel account
- GitHub repository connected to Vercel

### Steps

1. **Push to GitHub**: Ensure your code is pushed to your GitHub repository.

2. **Connect to Vercel**:
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import your GitHub repository

3. **Environment Variables**:
   - In Vercel project settings, go to "Environment Variables"
   - Add `REACT_APP_BACKEND_URL` with your backend API URL
   - Example: `https://api.hdmonks.com`

4. **Build Settings**:
   - Build Command: `npm install --legacy-peer-deps && npm run build`
   - Output Directory: `build`
   - Install Command: `npm install --legacy-peer-deps`

5. **Deploy**: Click "Deploy" and Vercel will automatically build and deploy your app.

### Important Notes

- The app uses `REACT_APP_BACKEND_URL` environment variable for API calls. Make sure it's set correctly on Vercel.
- All API requests are made from the frontend, so ensure your backend CORS settings allow requests from your Vercel domain.
- The build takes ~2-3 minutes initially.

## Project Structure

```
src/
├── components/       # Reusable React components
├── pages/           # Page components (Home, ServiceDetail)
├── lib/             # Utility functions
├── hooks/           # Custom React hooks
├── data/            # Mock data
├── App.js           # Main App component
└── index.js         # Entry point
```

## Tech Stack

- **React 19**: UI library
- **React Router 7**: Client-side routing
- **TailwindCSS 3**: CSS framework
- **Shadcn UI**: Component library
- **Axios**: HTTP client
- **React Hook Form**: Form management
- **Lucide React**: Icons
- **Zod**: Schema validation

## Common Issues & Solutions

### Build Error: "craco: not found"
Run `npm install --legacy-peer-deps` to install dependencies including craco.

### Build Error: "MODULE_NOT_FOUND"
Run `npm install --legacy-peer-deps` again, or `npm cache clean --force` and retry.

### API calls not working
- Verify `REACT_APP_BACKEND_URL` is set correctly
- Check backend CORS settings allow your frontend domain
- Ensure backend is running and accessible

### Vercel Build Fails
- Check "Deployment" logs in Vercel dashboard
- Ensure `REACT_APP_BACKEND_URL` environment variable is set
- Run `npm run build` locally first to verify it works

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
