// src/components/EnergyRecordList.jsx
import React, { useEffect, useState } from 'react';
import { getEnergyRecords } from '../api';

const EnergyRecordList = () => {
  const [records, setRecords] = useState([]);

  useEffect(() => {
    getEnergyRecords().then((response) => {
      setRecords(response.data);
    });
  }, []);

  return (
    <div>
      <h2>Energy Records</h2>
      <ul>
        {records.map((record) => (
          <li key={record.id}>{record.consumption}</li>
        ))}
      </ul>
    </div>
  );
};

export default EnergyRecordList;
