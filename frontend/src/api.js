// src/api.js
import axios from 'axios';

// Define base URL for API requests
const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

// Create axios instance
const api = axios.create({
  baseURL: API_URL,
});

// Define API endpoints
const login = (username, password) => api.post('/auth', { username, password });
const register = (username, password) => api.post('/user', { username, password });
const addEnergyRecord = (consumption) => api.post('/energy', { consumption });
const getEnergyRecords = () => api.get('/energy');
const getAnalytics = () => api.get('/analytics');

// Export API functions
export { login, register, addEnergyRecord, getEnergyRecords, getAnalytics };
