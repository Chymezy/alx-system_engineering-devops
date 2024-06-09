import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

export const register = (userData) => axios.post(`${API_URL}/users`, userData);
export const login = (userData) => axios.post(`${API_URL}/auth/login`, userData);
export const addEnergyRecord = (recordData) => axios.post(`${API_URL}/energy`, recordData);
export const getEnergyRecords = () => axios.get(`${API_URL}/energy`);
export const updateEnergyRecord = (recordId, recordData) => axios.put(`${API_URL}/energy/${recordId}`, recordData);
export const deleteEnergyRecord = (recordId) => axios.delete(`${API_URL}/energy/${recordId}`);
export const getAnalytics = (userId) => axios.get(`${API_URL}/analytics/${userId}`);
export const addAnalytics = (analyticsData) => axios.post(`${API_URL}/analytics`, analyticsData);
export const updateAnalytics = (analyticsId, analyticsData) => axios.put(`${API_URL}/analytics/${analyticsId}`, analyticsData);
export const deleteAnalytics = (analyticsId) => axios.delete(`${API_URL}/analytics/${analyticsId}`);

