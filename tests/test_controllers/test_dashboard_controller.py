#!/usr/bin/python3
"""Unittest get_dashboard_data"""

import unittest
from unittest.mock import patch, MagicMock
from app.utils.database import DatabaseUtils


class TestDatabaseUtils(unittest.TestCase):
    """Set up the test database connection
    Instantiate the DatabaseUtils with the test database connection """

    @patch('app.utils.database.db_connector.connect', autospec=True)
    def setUp(self, mock_db_connect):
        self.test_db = MagicMock()
        mock_db_connect.return_value = self.test_db

        self.database_utils = DatabaseUtils()

    def test_insert_employee(self):
        """Mock the cursor and execute methods
        test logic for inserting an employee
        """
        mock_cursor = self.test_db.cursor.return_value
        mock_cursor.execute.return_value = None
        employee_data = {'name': 'John Doe', 'position': 'Developer',
                         'department': 'IT', 'age': 30}
        result = self.database_utils.insert_employee(employee_data)

        self.assertTrue(result)
        mock_cursor.execute.
        assert_called_once_with("INSERT INTO employees (name, position, 
                                                        department, age) 
                                 VALUES (%s, %s, %s, %s)",
                               ('John Doe', 'Developer', 'IT', 30)
)

)

        )
        self.test_db.commit.assert_called_once()

    def tearDown(self):
        """Clean up resources, close connections, etc."""
        pass


if __name__ == '__main__':
    unittest.main()
