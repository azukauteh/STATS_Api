#!/usr/bin/python3
"""
Cotains DashboardService
"""
from app.models.employee_model import Employee
from app.models.attendance_model import Attendance


class DashboardService:
    def calculate_dashboard_stats(self):
        total_employees = Employee.query.count()
        present_count = Attendance.query.filter_by(status='Present').count()
        absent_count = Attendance.query.filter_by(status='Absent').count()

        stats = {
            'total_employees': total_employees,
            'present_count': present_count,
            'absent_count': absent_count
        }

        return stats
