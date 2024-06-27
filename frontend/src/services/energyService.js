import { addEnergyRecord, getEnergyRecords } from '../api';

// Importance: Abstracts API calls for energy records.

// Define function to add an energy record
const addEnergyRecordService = async (consumption) => {
  const response = await addEnergyRecord(consumption);
  // Handle add energy record response
  return response.data;
};

// Define function to get energy records
const getEnergyRecordsService = async () => {
  const response = await getEnergyRecords();
  // Handle get energy records response
  return response.data;
};

export { addEnergyRecordService, getEnergyRecordsService };

