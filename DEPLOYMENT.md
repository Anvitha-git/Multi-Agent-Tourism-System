# Deployment Guide

This document details deploying the Multi-Agent Tourism Planner:
- Backend (FastAPI) on Render
- Frontend (Vite + React) on Vercel

## 1. Backend (Render)

### 1.1. Repo & Files
Ensure `render.yaml` exists at repo root (already added). Render will detect and let you create the service.

### 1.2. Create Web Service
1. Log in to https://render.com
2. New + Web Service → Connect GitHub repo `Multi-Agent-Tourism-System`.
3. Render will read `render.yaml`. Confirm settings:
   - Build Command: `pip install -r backend/requirements.txt`
   - Start Command: `uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT`
   - Environment: Python 3.11
4. Click Create Web Service.

### 1.3. Environment Variables
You can add (optional):
- `LOG_LEVEL=info`
- Add any API keys if future features require.

### 1.4. CORS Configuration
`backend/app/main.py` includes CORSMiddleware. After first deploy, replace the placeholder origin in `allowed_origins` with your actual Vercel domain, e.g.:
```python
allowed_origins = [
    "https://your-vercel-domain.vercel.app",
    "http://localhost:5173"
]
```
Redeploy after editing.

### 1.5. Health Check
The `healthCheckPath: /docs` lets Render verify service availability via FastAPI docs endpoint.

### 1.6. Testing
Once deployed, backend base URL looks like:
```
https://multi-agent-tourism-backend.onrender.com
```
Test endpoint (replace with actual):
```
GET https://<render-domain>/api/v1/tourism/plan  (POST with JSON body)
```

## 2. Frontend (Vercel)

### 2.1. Project Setup
Option A (recommended): Import the same GitHub repo but set project root to `frontend` in Vercel UI (Monorepo setting).
Option B: Create a separate repo containing only the `frontend` folder.

### 2.2. Build Settings
Vercel automatically detects Vite:
- Install Command: `npm install`
- Build Command: `npm run build`
- Output Directory: `frontend/dist` (if root is repo, or just `dist` if root is `frontend`).

### 2.3. Environment Variable
Set `VITE_API_BASE_URL` under Project Settings → Environment Variables to your Render backend base:
```
VITE_API_BASE_URL=https://multi-agent-tourism-backend.onrender.com/api/v1/tourism
```
Rebuild after adding.

### 2.4. vercel.json
A simplified `vercel.json` exists to route built assets. Adjust if root directory differs:
If project root = `frontend`, you can remove the `routes` entry and use default.

### 2.5. Testing Frontend
Open the Vercel deployment URL; submit queries to verify responses. Use browser dev tools → Network panel to confirm calls to Render domain.

## 3. Local Environment & Parity
For local frontend pointing to local backend:
```
# In frontend/.env.local
VITE_API_BASE_URL=http://localhost:8000/api/v1/tourism
```
Frontend will automatically use this value due to updated `client.ts` logic.

## 4. Updates & Redeploys
- Push commits → Render auto-deploy (autoDeploy: true).
- Vercel auto-build on new commits to chosen branch.
- If you change allowed origins, modify `backend/app/main.py` and push.

## 5. Common Issues
| Issue | Cause | Fix |
|-------|-------|-----|
| CORS error | Missing production origin in `allowed_origins` | Add Vercel URL, redeploy backend |
| 404 on API | Wrong base URL env variable | Verify `VITE_API_BASE_URL` ends with `/api/v1/tourism` |
| Mixed content (HTTPS) | Backend served via HTTP | Ensure Render domain uses HTTPS |
| Large cold start delay | Free tier spin-up | Consider upgrading Render plan |

## 6. Optional Improvements
- Add GitHub Actions pipeline for tests before deployment.
- Add caching (Redis) for geocoding and attractions.
- Add OpenAPI client generation for stricter typing between front/back.
- Configure logging aggregation (e.g., Logtail) via environment variable.

## 7. Manual Deployment Commands (Fallback)
If Render build fails, use shell override:
```
pip install --upgrade pip
pip install -r backend/requirements.txt
uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT
```

## 8. Rollback Strategy
Render retains previous deploy images; use dashboard to rollback if a faulty commit breaks production. Vercel offers quick redeploy for prior build.

## 9. Checking Health After Deployment
```
# Backend docs
curl https://multi-agent-tourism-backend.onrender.com/docs

# Sample plan query
curl -X POST https://multi-agent-tourism-backend.onrender.com/api/v1/tourism/plan \
  -H "Content-Type: application/json" \
  -d '{"query":"plan my trip to Paris"}'
```
Expect JSON with both weather and places.

---
Deployment configuration complete. Adjust environment variable values post-deployment with actual generated URLs.
