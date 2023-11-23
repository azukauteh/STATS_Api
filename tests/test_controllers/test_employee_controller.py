#!/usr/bin/python3
""" unitestmodel Employee_Controller"""
import unittest
from unittest.mock import MagicMock, patch
from flask import Flask, jsonify
from app.controllers.employee_controller import EmployeeController


class TestEmployeeController(unittest.TestCase):
    """Unit tests for EmployeeController"""

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True

    def test_create_employee(self):
        employee_service_mock = MagicMock()
        with self.app.test_request_context('/'):
            employee_controller = EmployeeController(employee_service_mock)
            with patch('flask.request.json', return_value={'name': 'John Doe',
                       'position': 'Developer',
                       'department': 'IT','age': 30}):
                response = employee_controller.create_employee()
                self.assertEqual(response.status_code, 200)
                employee_service_mock.create_employee.
                assert_called_once_with(
                                        {'name': 'John Doe',
                                         'position': 'Developer',
                                         'department': 'IT', 'age': 30})

    def test_get_employee(self):employee_service_mock = MagicMock()
        with self.app.test_request_context('/'):
            employee_controller = EmployeeController(employee_service_mock)
            response = employee_controller.get_employee(1)
            self.assertEqual(response.status_code, 404)
            self.assertEqual(response.get_json(), {'message':
                                                   'Employee not found'})

    def test_update_employee(self):
        employee_service_mock = MagicMock()
        with self.app.test_request_context('/'):
            employee_controller = EmployeeController(employee_service_mock)
            with patch('flask.request.json', return_value={'name':
                                                           'Updated Name',
                                                           'position':
                                                           'Updated Position',
                                                           'department':
                                                           'Updated
                                                           Department',
                                                           'age': 35}):
                response = employee_controller.update_employee(1)
                self.assertEqual(response.status_code, 200)
                employee_service_mock.update_employee.
                assert_called_once_with(1, {'name': 'Updated Name',
                                        'position': 'Updated Position',
                                        'department': 'Updated Department',
                                        'age': 35})

    def test_delete_employee(self):
        employee_service_mock = MagicMock()
        with self.app.test_request_context('/'):
            employee_controller = EmployeeController(employee_service_mock)
            response = employee_controller.delete_employee(1)
            self.assertEqual(response.status_code, 200)
            employee_service_mock.delete_employee.assert_called_once_with(1)


if __name__ == '__main__':
    unittest.main()
