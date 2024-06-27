import React, { useState, useEffect } from 'react';
import { getAnalytics } from '../api';


// Importance: Displays analytics data for the user.

const Analytics = () => {
  const [analytics, setAnalytics] = useState([]);

  useEffect(() => {
    // Fetch analytics data from the API
    getAnalytics().then(response => setAnalytics(response.data));
  }, []);

  return (
    <div>
      <h1>Analytics</h1>
      <pre>{JSON.stringify(analytics, null, 2)}</pre>
    </div>
  );
};

export default Analytics;

