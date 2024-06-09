// src/components/Analytics.js

import React, { useEffect, useState } from 'react';
import { getAnalytics } from '../api';

const Analytics = ({ userId }) => {
    const [analytics, setAnalytics] = useState(null);

    useEffect(() => {
        const fetchAnalytics = async () => {
            try {
                const response = await getAnalytics(userId);
                setAnalytics(response.data);
            } catch (error) {
                console.error(error);
            }
        };
        fetchAnalytics();
    }, [userId]);

    return (
        <div>
            <h2>Analytics</h2>
            {analytics && (
                <div>
                    <p>Average Consumption: {analytics.averageConsumption}</p>
                    <p>Time Period: {analytics.timePeriod}</p>
                </div>
            )}
        </div>
    );
};

export default Analytics;

