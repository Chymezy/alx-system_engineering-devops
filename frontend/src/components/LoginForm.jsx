// import React, { useState } from 'react';
// import { login } from '../api';
// import { useNavigate } from 'react-router-dom';  // Use React Router v6 for navigation

// const LoginForm = () => {
//   const [username, setUsername] = useState('');
//   const [password, setPassword] = useState('');
//   const navigate = useNavigate();  // Initialize useNavigate

//   const handleSubmit = async (event) => {
//     event.preventDefault();
//     if (!username || !password) {
//       console.error('Username and password are required');
//       return;
//     }
    
//     try {
//       const response = await login(username, password);
//       const { access_token, refresh_token } = response.data;
//       localStorage.setItem('accessToken', access_token);
//       localStorage.setItem('refreshToken', refresh_token);
//       navigate('/energy_records');  // Redirect to energy records page
//     } catch (error) {
//       console.error('Login failed', error);
//       // Optionally set error state to display a message to the user
//     }
//   };

//   return (
//     <form onSubmit={handleSubmit}>
//       <h1>Login</h1>
//       <input
//         type="text"
//         value={username}
//         onChange={e => setUsername(e.target.value)}
//         placeholder="Username"
//       />
//       <input
//         type="password"
//         value={password}
//         onChange={e => setPassword(e.target.value)}
//         placeholder="Password"
//       />
//       <button type="submit">Login</button>
//     </form>
//   );
// };

// export default LoginForm;

import React, { useState } from 'react';
import { login } from '../api';
import { useNavigate } from 'react-router-dom';

const LoginForm = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!username || !password) {
      setErrorMessage('Username and password are required');
      return;
    }

    try {
      const response = await login(username, password);
      const { access_token, refresh_token } = response.data;
      localStorage.setItem('accessToken', access_token);
      localStorage.setItem('refreshToken', refresh_token);
      navigate('/welcome');  // Redirect to welcome page
    } catch (error) {
      setErrorMessage('Login failed');
      console.error('Login failed', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h1>Login</h1>
      <input
        type="text"
        value={username}
        onChange={e => setUsername(e.target.value)}
        placeholder="Username"
      />
      <input
        type="password"
        value={password}
        onChange={e => setPassword(e.target.value)}
        placeholder="Password"
      />
      <button type="submit">Login</button>
      {errorMessage && <p style={{ color: 'red' }}>{errorMessage}</p>}
    </form>
  );
};

export default LoginForm;
