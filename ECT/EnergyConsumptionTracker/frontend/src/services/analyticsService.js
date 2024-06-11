import { getAnalytics } from '../api';


//Importance: Abstracts API calls for analytics data.
// Define function to get analytics data
const getAnalyticsService = async () => {
  const response = await getAnalytics();
  // Handle get analytics response
  return response.data;
};

export { getAnalyticsService };

