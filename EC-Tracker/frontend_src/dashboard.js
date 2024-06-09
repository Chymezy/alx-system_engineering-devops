// src/components/Dashboard.js

import React, { useEffect, useState } from 'react';
import { getEnergyRecords } from '../api';

const Dashboard = () => {
    const [energyRecords, setEnergyRecords] = useState([]);

    useEffect(() => {
        const fetchEnergyRecords = async () => {
            try {
                const response = await getEnergyRecords();
                setEnergyRecords(response.data);
            } catch (error) {
                console.error(error);
            }
        };
        fetchEnergyRecords();
    }, []);

    return (
        <div>
            <h2>Dashboard</h2>
            <ul>
                {energyRecords.map(record => (
                    <li key={record.recordId}>
                        Date: {record.date}, Consumption: {record.consumption}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Dashboard;

