import React from 'react';
import { Box, Typography, Container } from '@mui/material';

const About = () => {
  return (
    <Container>
      <Box sx={{ py: 5, textAlign: 'center' }}>
        <Typography variant="h4" component="h2" gutterBottom>
          About Energy Manager
        </Typography>
        <Typography variant="body1">
          Energy Manager helps you track and manage your energy consumption efficiently, saving you time and money.
        </Typography>
      </Box>
    </Container>
  );
};

export default About;
