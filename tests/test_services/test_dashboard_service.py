#!/usr/bin/python3
"""
Contains tests for DashboardService
"""
import unittest
from unittest.mock import patch, MagicMock
from app.services.dashboard_service import DashboardService


class TestDashboardService(unittest.TestCase):
    def setUp(self):
        """ Set up  context or configuration"""
        pass

    def tearDown(self):
        """ Clean up any resources or configurations after each test"""
        pass

    @patch('app.services.dashboard_service.Employee')
    @patch('app.services.dashboard_service.Attendance')
    def test_calculate_dashboard_stats(self, mock_attendance, mock_employee):
        """ Mock the necessary methods for Employee and Attendance queries"""
        mock_employee.query.count.return_value = 10
        mock_attendance.query.filter_by.return_value.count.side_effect = [5, 3]

        """ Create  instance of DashboardService"""
        dashboard_service = DashboardService()

        """ invoke calculate_dashboard_stats method"""
        stats = dashboard_service.calculate_dashboard_stats()

        """ Verify that the stats dictionary is created correctly"""
        self.assertEqual(stats['total_employees'], 10)
        self.assertEqual(stats['present_count'], 5)
        self.assertEqual(stats['absent_count'], 3)


if __name__ == '__main__':
    unittest.main()
