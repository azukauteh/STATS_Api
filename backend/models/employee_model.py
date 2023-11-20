#!/usr/bin/python3
"""Defines an Employee class"""

from datetime import datetime


class Employee:
    """Employee attributes"""
    def __init__(self, employee_id, name, position,
                 department, age, hire_date=None):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.department = department
        self.age = age
        self.hire_date = hire_date or datetime.now().strftime('%Y-%m-%d')

    def to_dict(self):
        return {
            'employee_id': self.employee_id,
            'name': self.name,
            'position': self.position,
            'department': self.department,
            'age': self.age,
            'hire_date': self.hire_date
        }
