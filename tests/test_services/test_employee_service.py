#!/usr/bin/python3
"""
Contains tests for EmployeeService
"""
import unittest
from unittest.mock import patch, MagicMock
from app.services.employee_service import EmployeeService
from app.models.employee_model import Employee
from app.utils.database import db


class TestEmployeeService(unittest.TestCase):
    def setUp(self):
        """ Set up context or configuration"""
        pass

    def tearDown(self):
        """ Clean up any resources or configurations"""
        pass

    @patch('app.services.employee_service.Employee')
    @patch('app.services.employee_service.db')
    def test_get_employee_details(self, mock_db, mock_employee):
        """ Mock the query method of Employee"""
        mock_employee.query.get.return_value = MagicMock(
                                                       to_dict=MagicMock(
        return_value={'employee_id': 1, 'name': 'John Doe'}
    )
)

        """  instance of EmployeeService"""
        employee_service = EmployeeService()

        """ Call the get_employee_details method"""
        result = employee_service.get_employee_details(1)

        """ Verify that the result is as expected"""
        self.assertEqual(result, {'employee_id': 1, 'name': 'John Doe'})

    @patch('app.services.employee_service.Employee')
    @patch('app.services.employee_service.db')
    def test_create_employee(self, mock_db, mock_employee):
        # Mock the necessary methods for database interaction
        mock_db.session.add.return_value = None
        mock_db.session.commit.return_value = None
        mock_employee.return_value = MagicMock(`o_dict=MagicMock
                                              (return_value={'employee_id': 1, 
                                                             'name':
                                                             'John Doe'}))

        """ceate an instance of EmployeeService"""
        employee_service = EmployeeService()

        """ Call the create_employee method"""
        result = employee_service.create_employee({'name': 'John Doe',
                                                   'position': 'Developer',
                                                   'department': 'IT',
                                                   'age': 30})

        """ Verify that the result is as expected"""
        self.assertEqual(result, {'employee_id': 1, 'name': 'John Doe'})


if __name__ == '__main__':
    unittest.main()
