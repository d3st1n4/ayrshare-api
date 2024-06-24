import unittest
from unittest.mock import patch, MagicMock
import requests
import sqlalchemy as db
import pandas as pd
import os
from API import get_account_info, post_tweet, save_to_database  # Import functions from API.py

class TestAPIRequests(unittest.TestCase):

    @patch('API.requests.get')  # Patch the requests.get call in API.py
    def test_get_account_info(self, mock_get):
        # Normal case
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"account": "details"}
        mock_get.return_value = mock_response

        response = get_account_info("valid_api_key")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"account": "details"})

        # Edge case: invalid api key
        mock_response.status_code = 401
        mock_response.json.return_value = {"error": "unauthorized"}
        mock_get.return_value = mock_response

        response = get_account_info("invalid_api_key")
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"error": "unauthorized"})

    @patch('API.requests.post')  # Patch the requests.post call in API.py
    def test_post_tweet(self, mock_post):
        # Normal case
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"post": "successful"}
        mock_post.return_value = mock_response

        payload = {
            "post": "Today is a great day!",
            "platforms": ["twitter"],
            "mediaUrls": ["https://img.ayrshare.com/012/gb.jpg"]
        }
        response = post_tweet("valid_api_key", payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"post": "successful"})

        # Edge case: invalid api key
        mock_response.status_code = 401
        mock_response.json.return_value = {"error": "unauthorized"}
        mock_post.return_value = mock_response

        response = post_tweet("invalid_api_key", payload)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"error": "unauthorized"})

class TestDatabaseOperations(unittest.TestCase):

    @patch('API.db.create_engine')  # Patch the create_engine call in API.py
    def test_save_to_database(self, mock_create_engine):
        # Mock the engine and connection
        mock_engine = MagicMock()
        mock_connection = MagicMock()
        mock_create_engine.return_value = mock_engine
        mock_engine.connect.return_value.__enter__.return_value = mock_connection
        
        # Mock the dataframe and query result
        mock_df = MagicMock()
        mock_connection.execute.return_value.fetchall.return_value = [("result_row",)]
        
        data_dict = {
            "post": "Today is a great day!",
            "platforms": ["twitter"],
            "mediaUrls": ["https://img.ayrshare.com/012/gb.jpg"]
        }
        
        result = save_to_database(data_dict, 'data_base_name', 'table_name')
        self.assertIsInstance(result, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()
