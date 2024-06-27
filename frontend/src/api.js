// // src/api.js
// import axios from 'axios';

// // Define base URL for API requests
// const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

// // Create axios instance
// const api = axios.create({
//   baseURL: API_URL,
// });

// // Define API endpoints
// const login = (username, password) => api.post('/auth', { username, password });
// const register = (username, password) => api.post('/user', { username, password });
// const addEnergyRecord = (consumption) => api.post('/energy', { consumption });
// const getEnergyRecords = () => api.get('/energy');
// const getAnalytics = () => api.get('/analytics');

// // Export API functions
// export { login, register, addEnergyRecord, getEnergyRecords, getAnalytics };

// src/api.js
import axios from 'axios';

// Define base URL for API requests
const API_URL = import.meta.env.VITE_REACT_APP_API_URL || 'http://localhost:4444/api';

// Create axios instance
const api = axios.create({
  baseURL: API_URL,
});

// Intercept requests to include the Authorization header with the access token
api.interceptors.request.use(config => {
  const token = localStorage.getItem('accessToken');
  if (token) {
    config.headers['Authorization'] = `Bearer ${token}`;
  }
  return config;
}, error => {
  return Promise.reject(error);
});

// Intercept responses to handle token refresh logic
api.interceptors.response.use(response => {
  return response;
}, async error => {
  const originalRequest = error.config;
  if (error.response.status === 401 && !originalRequest._retry) {
    originalRequest._retry = true;
    const newAccessToken = await refreshAccessToken();
    if (newAccessToken) {
      originalRequest.headers['Authorization'] = `Bearer ${newAccessToken}`;
      return api(originalRequest);
    }
  }
  return Promise.reject(error);
});

// Define token refresh function
const refreshAccessToken = async () => {
  const refreshToken = localStorage.getItem('refreshToken');
  try {
    const response = await api.post('/auth/refresh', { refresh_token: refreshToken });
    const { access_token } = response.data;
    localStorage.setItem('accessToken', access_token);
    return access_token;
  } catch (error) {
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
    return null;
  }
};

// Define API endpoints
const login = (username, password) => api.post('/auth/login', { username, password });
const register = (username, password) => api.post('/user', { username, password });
const addEnergyRecord = (consumption) => api.post('/energy_records', { consumption });
const getEnergyRecords = () => api.get('/energy_records');
const getAnalytics = () => api.get('/analytics');

// Export API functions
export { login, register, addEnergyRecord, getEnergyRecords, getAnalytics };
