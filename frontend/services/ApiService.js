const ApiService = {
  getDashboardData: async () => {
    try {
      const response = await fetch('/api/dashboard');
      const data = await response.json();
      return data;
    } catch (error) {
      throw new Error('Error fetching dashboard data');
    }
  },
  //  more API calls more features
};

export default ApiService;

