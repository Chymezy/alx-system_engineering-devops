const API_BASE_URL = 'http://localhost:5000/api';

// User Authentication
export const loginUser = async (username, password) => {
    const response = await fetch(`${API_BASE_URL}/auth/login`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
    });
    return await response.json();
};

export const registerUser = async (username, email, password) => {
    const response = await fetch(`${API_BASE_URL}/users`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, email, password }),
    });
    return await response.json();
};

// Energy Records
export const addEnergyRecord = async (token, date, consumption) => {
    const response = await fetch(`${API_BASE_URL}/energy`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`,
        },
        body: JSON.stringify({ date, consumption }),
    });
    return await response.json();
};

export const getEnergyRecords = async (token) => {
    const response = await fetch(`${API_BASE_URL}/energy`, {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`,
        },
    });
    return await response.json();
};

export const getEnergyRecord = async (token, recordId) => {
    const response = await fetch(`${API_BASE_URL}/energy/${recordId}`, {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`,
        },
    });
    return await response.json();
};

export const updateEnergyRecord = async (token, recordId, date, consumption) => {
    const response = await fetch(`${API_BASE_URL}/energy/${recordId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`,
        },
        body: JSON.stringify({ date, consumption }),
    });
    return await response.json();
};

export const deleteEnergyRecord = async (token, recordId) => {
    const response = await fetch(`${API_BASE_URL}/energy/${recordId}`, {
        method: 'DELETE',
        headers: {
            'Authorization': `Bearer ${token}`,
        },
    });
    return await response.json();
};

// Analytics
export const getAnalytics = async (token) => {
    const response = await fetch(`${API_BASE_URL}/analytics`, {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`,
        },
    });
    return await response.json();
};

