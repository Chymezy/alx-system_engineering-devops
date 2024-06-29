import React from 'react';
import { NavLink, useLocation } from 'react-router-dom';
import { AppBar, Toolbar, Typography, Button, Box } from '@mui/material';
import logo from '../assets/logo.svg'; // Replace with your logo path

const Navbar = () => {
  const location = useLocation();

  return (
    <AppBar position="fixed" sx={{ backgroundColor: '#f5f5f5', color: '#333' }}>
      <Toolbar>
        <Box component="img" src={logo} alt="Energy Manager Logo" sx={{ height: 40, marginRight: 2 }} />
        <Typography variant="h6" sx={{ flexGrow: 1, color: '#333' }}>
          Energy Manager
        </Typography>
        <Button color="inherit" sx={{ margin: '0 8px' }}>
          <NavLink 
            to="/" 
            exact="true"
            className={location.pathname === '/' ? 'active-link' : ''}
          >
            Home
          </NavLink>
        </Button>
        <Button color="inherit" sx={{ margin: '0 8px' }}>
          <NavLink 
            to="/features" 
            className={location.pathname === '/welcome' ? 'active-link' : ''}
          >
            Features
          </NavLink>
        </Button>
        <Button color="inherit" sx={{ margin: '0 8px' }}>
          <NavLink 
            to="/about" 
            className={location.pathname === '/welcome' ? 'active-link' : ''}
          >
            About
          </NavLink>
        </Button>
        <Button color="inherit" sx={{ margin: '0 8px' }}>
          <NavLink 
            to="/login" 
            className={location.pathname === '/login' ? 'active-link' : ''}
          >
            Login
          </NavLink>
        </Button>
        <Button color="inherit" sx={{ margin: '0 8px' }}>
          <NavLink 
            to="/welcome" 
            className={location.pathname === '/welcome' ? 'active-link' : ''}
          >
            Welcome
          </NavLink>
        </Button>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
