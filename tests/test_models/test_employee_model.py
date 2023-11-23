#!/usr/bin/python3
"""
Contains tests for Employee
"""
import unittest
from app.models.employee_model import Employee
from datetime import datetime


class TestEmployee(unittest.TestCase):
    def setUp(self):
        """ Set up any necessary mocks or configurations"""
        pass

    def tearDown(self):
        """ Clean up resources"""
        pass

    def test_to_dict(self):
        """ Create instance of the Employee with an appropriate date"""
        hire_date = datetime(2023, 11, 10)
        employee = Employee(employee_id=1, name='John Doe',
                            position= 'Developer',department='IT', age=30,
                            hire_date=hire_date)

        """ invoke  to_dict method"""
        employee_dict = employee.to_dict()

        """ Verify that the dictionary is created correctly"""
        self.assertEqual(employee_dict['employee_id'], 1)
        self.assertEqual(employee_dict['name'], 'John Doe')
        self.assertEqual(employee_dict['position'], 'Developer')
        self.assertEqual(employee_dict['department'], 'IT')
        self.assertEqual(employee_dict['age'], 30)
        self.assertEqual(employee_dict['hire_date'],
                         hire_date.strftime('%Y-%m-%d'))


if __name__ == '__main__':
    unittest.main()
