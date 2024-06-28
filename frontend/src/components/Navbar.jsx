import React from 'react';
import { NavLink, useLocation } from 'react-router-dom';
import { AppBar, Toolbar, Typography, Button, Box } from '@mui/material';
import logo from '../assets/logo.svg'; // Adjust the path to your logo

const Navbar = () => {
  const location = useLocation();

  return (
    <AppBar 
      position="static" 
      sx={{ backgroundColor: '#ffffff', color: '#333', boxShadow: 'none', borderBottom: '1px solid #e0e0e0' }}
    >
      <Toolbar>
        <Box sx={{ display: 'flex', alignItems: 'center', flexGrow: 1 }}>
          <img 
            src={logo} 
            alt="Energy Manager" 
            style={{ height: '40px', marginRight: '10px' }} 
          />
          <Typography 
            variant="h6" 
            component="div" 
            sx={{ color: '#333', fontWeight: 'bold' }}
          >
            Energy Manager
          </Typography>
        </Box>
        <Box sx={{ display: 'flex', gap: '10px' }}>
          <Button 
            color="inherit" 
            component={NavLink} 
            to="/" 
            className={location.pathname === '/' ? 'active-link' : ''}
          >
            Home
          </Button>
          <Button 
            color="inherit" 
            component={NavLink} 
            to="/login" 
            className={location.pathname === '/login' ? 'active-link' : ''}
          >
            Login
          </Button>
          <Button 
            color="inherit" 
            component={NavLink} 
            to="/welcome" 
            className={location.pathname === '/welcome' ? 'active-link' : ''}
          >
            Welcome
          </Button>
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
