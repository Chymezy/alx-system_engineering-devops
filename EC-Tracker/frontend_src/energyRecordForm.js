// src/components/EnergyRecordForm.js

import React, { useState } from 'react';
import { addEnergyRecord, updateEnergyRecord } from '../api';

const EnergyRecordForm = ({ existingRecord }) => {
    const [date, setDate] = useState(existingRecord ? existingRecord.date : '');
    const [consumption, setConsumption] = useState(existingRecord ? existingRecord.consumption : '');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            if (existingRecord) {
                await updateEnergyRecord(existingRecord.recordId, { date, consumption });
                alert('Energy record updated successfully!');
            } else {
                await addEnergyRecord({ date, consumption });
                alert('Energy record added successfully!');
            }
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="date"
                value={date}
                onChange={(e) => setDate(e.target.value)}
                required
            />
            <input
                type="number"
                value={consumption}
                onChange={(e) => setConsumption(e.target.value)}
                required
            />
            <button type="submit">{existingRecord ? 'Update' : 'Add'} Record</button>
        </form>
    );
};

export default EnergyRecordForm;

