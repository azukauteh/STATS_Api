#!/usr/bin/python3
"""Defines an Attendance class"""

from datetime import datetime


class Attendance:
    """Attendance attributes"""
    def __init__(self, employee_id, date, status):
        self.employee_id = employee_id
        self.date = date
        self.status = status

    def to_dict(self):
        return {
            'employee_id': self.employee_id,
            'date': self.date,
            'status': self.status
        }
