// src/components/Welcome.jsx

import React from 'react';
import { Container, Box, Typography, List, ListItem, Paper } from '@mui/material';
import styled from '@emotion/styled';

const ContainerStyled = styled(Container)({
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  marginTop: '20px',
});

const PaperStyled = styled(Paper)({
  padding: '20px',
  backgroundColor: '#f5f5f5',
  height: '100vh',
});

const TypographyStyled = styled(Typography)({
  marginBottom: '20px',
});

const Welcome = () => {
  const energyEfficiencyTips = [
    "Tip 1: Turn off lights when not in use.",
    "Tip 2: Use energy-efficient appliances.",
    "Tip 3: Unplug devices when they're not being used.",
    "Tip 4: Use programmable thermostats.",
  ];

  return (
    <ContainerStyled>
      <Typography variant="h4" gutterBottom>Welcome to Energy Manager</Typography>
      <TypographyStyled variant="h6">Energy Efficiency Tips</TypographyStyled>
      <PaperStyled>
        <List>
          {energyEfficiencyTips.map((tip, index) => (
            <ListItem key={index}>{tip}</ListItem>
          ))}
        </List>
      </PaperStyled>
    </ContainerStyled>
  );
};

export default Welcome;
