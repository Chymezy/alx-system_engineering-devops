import React, { useState, useEffect } from 'react';
import { getEnergyRecords } from '../api';

// Importance: Displays a list of energy records.

const EnergyRecordList = () => {
  const [records, setRecords] = useState([]);

  useEffect(() => {
    // Fetch energy records from the API
    getEnergyRecords().then(response => setRecords(response.data));
  }, []);

  return (
    <div>
      <h1>Energy Records</h1>
      <ul>
        {records.map(record => (
          <li key={record.id}>{record.consumption} kWh on {record.recorded_at}</li>
        ))}
      </ul>
    </div>
  );
};

export default EnergyRecordList;

