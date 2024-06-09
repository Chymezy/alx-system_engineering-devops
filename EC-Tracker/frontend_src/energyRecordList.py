// src/components/EnergyRecordList.js

import React from 'react';
import { deleteEnergyRecord } from '../api';

const EnergyRecordList = ({ records, onEdit }) => {
    const handleDelete = async (recordId) => {
        try {
            await deleteEnergyRecord(recordId);
            alert('Energy record deleted successfully!');
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <ul>
            {records.map(record => (
                <li key={record.recordId}>
                    Date: {record.date}, Consumption: {record.consumption}
                    <button onClick={() => onEdit(record)}>Edit</button>
                    <button onClick={() => handleDelete(record.recordId)}>Delete</button>
                </li>
            ))}
        </ul>
    );
};

export default EnergyRecordList;

