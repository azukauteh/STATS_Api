#!/usr/bin/python3
"""
Contains tests for Attendance
"""
import unittest
from app.models.attendance_model import Attendance


class TestAttendance(unittest.TestCase):
    def setUp(self):
        """ Set up mocks or configurations"""
        pass

    def tearDown(self):
        """ Clean up resources"""
        pass

    def test_to_dict(self):
        """ Create an instance of  Attendance class"""
        attendance = Attendance(employee_id=1, date='2023-11-10',
                                status='Present')

        """ invoke the to_dict method"""
        attendance_dict = attendance.to_dict()

        """ Verify that the dictionary is created correctly"""
        self.assertEqual(attendance_dict['employee_id'], 1)
        self.assertEqual(attendance_dict['date'], '2023-11-10')
        self.assertEqual(attendance_dict['status'], 'Present')


if __name__ == '__main__':
    unittest.main()
