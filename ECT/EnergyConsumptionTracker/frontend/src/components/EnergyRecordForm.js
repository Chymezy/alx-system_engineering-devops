import React, { useState } from 'react';
import { addEnergyRecord } from '../api';


// Importance: Provides a form to add new energy records

const EnergyRecordForm = () => {
  const [consumption, setConsumption] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    // Add energy record via the API
    addEnergyRecord(consumption).then(() => setConsumption(''));
  };

  return (
    <form onSubmit={handleSubmit}>
      <h1>Add Energy Record</h1>
      <input
        type="number"
        value={consumption}
        onChange={e => setConsumption(e.target.value)}
        placeholder="Enter energy consumption"
      />
      <button type="submit">Add Record</button>
    </form>
  );
};

export default EnergyRecordForm;

