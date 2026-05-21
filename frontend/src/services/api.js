import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_URL,
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const login = (username, password) => {
  const formData = new URLSearchParams();
  formData.append('username', username);
  formData.append('password', password);
  return api.post('/auth/login', formData, {
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
  });
};

export const register = (email, username, password) => {
  return api.post('/auth/register', { email, username, password });
};

export const getMe = () => {
  return api.get('/auth/me');
};

export const predict = (text) => {
  return api.post('/predict/', { text });
};

export const getHistory = () => {
  return api.get('/dashboard/history');
};

export const getStats = () => {
  return api.get('/dashboard/stats');
};

export default api;
