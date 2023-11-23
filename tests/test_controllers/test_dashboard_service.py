#!/usr/bin/python3
"""
Contains tests for DashboardService
"""
import unittest
from unittest.mock import MagicMock, patch
from app.models.employee_model import Employee
from app.models.attendance_model import Attendance
from app.services.dashboard_service import DashboardService


class TestDashboardService(unittest.TestCase):
    def setUp(self):
        """ Set up any necessary mocks or configurations"""
        pass

    def tearDown(self):
        """Clean up resources"""
        pass

    @patch('app.models.employee_model.Employee.query')
    @patch('app.models.attendance_model.Attendance.query')
    def test_calculate_dashboard_stats(self, mock_employee_query,
                                       mock_attendance_query):
        """ Mock the count method for Employee and Attendance queries"""
        mock_employee_query.count.return_value = 10
        mock_attendance_query.filter_by().count.side_effect = [5, 3]
        dashboard_service = DashboardService()

        """ Call the method to calculate dashboard stats"""
        stats = dashboard_service.calculate_dashboard_stats()

        """ Verify that the counts are used correctly"""
        self.assertEqual(stats['total_employees'], 10)
        self.assertEqual(stats['present_count'], 5)
        self.assertEqual(stats['absent_count'], 3)


if __name__ == '__main__':
    unittest.main()
