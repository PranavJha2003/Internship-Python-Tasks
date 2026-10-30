import unittest
from unittest.mock import Mock, patch

import requests

from api_client import fetch_users


class TestFetchUsers(unittest.TestCase):

    @patch("api_client.requests.get")
    def test_fetch_users_returns_json(self, mock_get):

        expected = [
            {"id": 1, "name": "Leanne Graham"}
        ]

        mock_response = Mock()
        mock_response.json.return_value = expected
        mock_response.raise_for_status.return_value = None

        mock_get.return_value = mock_response

        result = fetch_users()

        self.assertEqual(result, expected)
    @patch("api_client.requests.get")
    def test_fetch_users_handles_http_error(self, mock_get):

        mock_response = Mock()

        mock_response.raise_for_status.side_effect = (
            requests.exceptions.HTTPError("404 Not Found")
        )

        mock_get.return_value = mock_response

        with self.assertRaises(requests.exceptions.HTTPError):
            fetch_users()


    @patch("api_client.requests.get")
    def test_fetch_users_rejects_invalid_json_structure(self, mock_get):

        mock_response = Mock()

        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {"error": "Invalid response"}

        mock_get.return_value = mock_response

        with self.assertRaises(ValueError):
            fetch_users()

if __name__ == "__main__":
    unittest.main()