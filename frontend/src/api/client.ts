import axios from 'axios';

// Resolve API base URL:
// 1. VITE_API_BASE_URL (set in Vercel dashboard or .env.local)
// 2. If absent, try window origin + '/api/v1/tourism'
// 3. Fallback to relative '/api/v1/tourism'
const envBase = import.meta.env.VITE_API_BASE_URL as string | undefined;
const derivedBase = typeof window !== 'undefined'
  ? `${window.location.origin}/api/v1/tourism`
  : '/api/v1/tourism';
const baseURL = envBase || derivedBase || '/api/v1/tourism';

const api = axios.create({
  baseURL,
  timeout: 10000,
});

export default api;
