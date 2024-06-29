import React from 'react';
import { Box, Typography, Container, Grid } from '@mui/material';

const Features = () => {
  return (
    <Container>
      <Box sx={{ py: 5, textAlign: 'center' }}>
        <Typography variant="h4" component="h2" gutterBottom>
          Features
        </Typography>
        <Grid container spacing={3}>
          <Grid item xs={12} md={4}>
            <Box sx={{ p: 2, backgroundColor: '#f5f5f5', borderRadius: '8px', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)' }}>
              <Typography variant="h6" component="h3" gutterBottom>
                Feature 1
              </Typography>
              <Typography variant="body1">
                Description of feature 1.
              </Typography>
            </Box>
          </Grid>
          <Grid item xs={12} md={4}>
            <Box sx={{ p: 2, backgroundColor: '#f5f5f5', borderRadius: '8px', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)' }}>
              <Typography variant="h6" component="h3" gutterBottom>
                Feature 2
              </Typography>
              <Typography variant="body1">
                Description of feature 2.
              </Typography>
            </Box>
          </Grid>
          <Grid item xs={12} md={4}>
            <Box sx={{ p: 2, backgroundColor: '#f5f5f5', borderRadius: '8px', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)' }}>
              <Typography variant="h6" component="h3" gutterBottom>
                Feature 3
              </Typography>
              <Typography variant="body1">
                Description of feature 3.
              </Typography>
            </Box>
          </Grid>
        </Grid>
      </Box>
    </Container>
  );
};

export default Features;
