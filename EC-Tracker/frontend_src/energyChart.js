import React from 'react';
import { Line } from 'react-chartjs-2';

const EnergyChart = ({ records }) => {
  const data = {
    labels: records.map(record => record.date),
    datasets: [
      {
        label: 'Energy Consumption',
        data: records.map(record => record.consumption),
        borderColor: 'rgba(75,192,192,1)',
        borderWidth: 2,
        fill: false,
      },
    ],
  };

  return <Line data={data} />;
};

export default EnergyChart;

