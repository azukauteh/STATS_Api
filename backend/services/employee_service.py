#!/usr/bin/python3
"""
Contains employee_service.py
"""
from app.models.employee_model import Employee
from app.utils.database import db


class EmployeeService:
    def get_employee_details(self, employee_id):
        employee = Employee.query.get(employee_id)
        if not employee:
            return None  """ Return None if the employee doesn't exist"""
        return employee.to_dict()

    def create_employee(self, data):
        new_employee = Employee(**data)
        db.session.add(new_employee)
        db.session.commit()
        return new_employee.to_dict()
