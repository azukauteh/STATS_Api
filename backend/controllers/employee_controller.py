#!/usr/bin/python3
"""
employee_controller
"""
from flask import Blueprint, jsonify, request
from app.services.employee_service import EmployeeService


class EmployeeController:
    def __init__(self, employee_service):
        self.employee_service = employee_service

    def create_employee(self):
        data = request.json
        result = self.employee_service.create_employee(data)
        return jsonify(result)

    def get_employee(self, employee_id):
        employee = self.employee_service.get_employee(employee_id)
        if employee:
            return jsonify(employee)
        else:
            return jsonify({'message': 'Employee not found'}), 404

    def update_employee(self, employee_id):
        data = request.json
        result = self.employee_service.update_employee(employee_id, data)
        return jsonify(result)

    def delete_employee(self, employee_id):
        result = self.employee_service.delete_employee(employee_id)
        return jsonify(result)
