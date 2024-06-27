import React, { useState, useEffect } from 'react';
import { getEnergyRecords, addEnergyRecord } from '../api';
import { Container, Box, TextField, Button, Typography, List, ListItem, Paper, Grid } from '@mui/material';
import { styled } from '@mui/system';  // Updated import

const useStyles = styled({
  container: {
    display: 'flex',
    marginTop: '20px',
  },
  form: {
    marginBottom: '20px',
  },
  sidebar: {
    padding: '20px',
    backgroundColor: '#f5f5f5',
    height: '100vh',
  },
  content: {
    flexGrow: 1,
  },
  tips: {
    marginBottom: '20px',
  },
});

const EnergyRecordList = () => {
  const classes = useStyles();
  const [records, setRecords] = useState([]);
  const [consumption, setConsumption] = useState('');
  const [recordedAt, setRecordedAt] = useState('');

  useEffect(() => {
    // Fetch energy records from the API
    getEnergyRecords().then(response => setRecords(response.data));
  }, []);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const newRecord = {
      consumption,
      recorded_at: recordedAt,
    };
    const response = await addEnergyRecord(newRecord);
    setRecords([...records, response.data]);
    setConsumption('');
    setRecordedAt('');
  };

  const energyEfficiencyTips = [
    "Tip 1: Turn off lights when not in use.",
    "Tip 2: Use energy-efficient appliances.",
    "Tip 3: Unplug devices when they're not being used.",
    "Tip 4: Use programmable thermostats.",
  ];

  return (
    <Container className={classes.container}>
      <Box className={classes.sidebar} component={Paper}>
        <Typography variant="h6" className={classes.tips}>Energy Efficiency Tips</Typography>
        <List>
          {energyEfficiencyTips.map((tip, index) => (
            <ListItem key={index}>{tip}</ListItem>
          ))}
        </List>
      </Box>
      <Box className={classes.content}>
        <Typography variant="h4" gutterBottom>Energy Records</Typography>
        <form className={classes.form} onSubmit={handleSubmit}>
          <TextField
            label="Consumption (kWh)"
            type="number"
            value={consumption}
            onChange={(e) => setConsumption(e.target.value)}
            fullWidth
            margin="normal"
            required
          />
          <TextField
            label="Recorded At"
            type="datetime-local"
            value={recordedAt}
            onChange={(e) => setRecordedAt(e.target.value)}
            fullWidth
            margin="normal"
            InputLabelProps={{
              shrink: true,
            }}
            required
          />
          <Button type="submit" variant="contained" color="primary" fullWidth> Add Record </Button>
        </form>
        <List>
          {records.map(record => (
            <ListItem key={record.id}>{record.consumption} kWh on {record.recorded_at}</ListItem>
          ))}
        </List>
      </Box>
    </Container>
  );
};

export default EnergyRecordList;
