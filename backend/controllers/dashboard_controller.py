#!/usr/bin/python3
"""
dashboard_controller.py
"""
from flask import Blueprint, jsonify
from app.services.dashboard_service import DashboardService


class DashboardController:
    def __init__(self, dashboard_service):
        self.dashboard_service = dashboard_service

    def get_dashboard_stats(self):
        stats = self.dashboard_service.calculate_dashboard_stats()
        return jsonify(stats)
