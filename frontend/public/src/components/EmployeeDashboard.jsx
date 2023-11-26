import React, { useState, useEffect } from 'react';
import ApiService from '../services/ApiService';

const EmployeeDashboard = () => {
  const [dashboardData, setDashboardData] = useState(null);

  useEffect(() => {
    // Fetch dashboard data on component mount
    ApiService.getDashboardData()
      .then(data => setDashboardData(data))
      .catch(error => console.error('Error fetching dashboard data:', error));
  }, []);

  return (
    <div>
      <h2>Employee Dashboard</h2>
      {dashboardData ? (
        <div>
          <p>Total Employees: {dashboardData.total_employees}</p>
          <p>Present Employees: {dashboardData.present_count}</p>
          <p>Absent Employees: {dashboardData.absent_count}</p>
        </div>
      ) : (
        <p>Loading dashboard data...</p>
      )}
    </div>
  );
};

export default EmployeeDashboard;
