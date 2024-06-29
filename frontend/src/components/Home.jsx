import React from 'react';
import { Box, Typography, Button, Container } from '@mui/material';
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <Container>
      <Box
        sx={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          height: '80vh',
          textAlign: 'center',
          backgroundColor: '#f5f5f5',
          padding: '20px',
          borderRadius: '8px',
          boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
        }}
      >
        <Typography variant="h2" component="h1" gutterBottom>
          Energy Manager
        </Typography>
        <Typography variant="h5" component="h2" gutterBottom>
          Track and Manage Your Energy Consumption Efficiently
        </Typography>
        <Button variant="contained" color="primary" component={Link} to="/login" sx={{ mt: 3 }}>
          Get Started
        </Button>
      </Box>
    </Container>
  );
};

export default Home;
