import { login, register } from '../api';

// Importance: Abstracts API calls for authentication.

// Define function to perform login
const loginService = async (username, password) => {
  const response = await login(username, password);
  // Handle login response
  return response.data;
};

// Define function to perform registration
const registerService = async (username, password) => {
  const response = await register(username, password);
  // Handle registration response
  return response.data;
};

export { loginService, registerService };

