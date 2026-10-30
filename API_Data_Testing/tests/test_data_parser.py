import unittest
import tempfile
from pathlib import Path

from data_parser import parse_users, save_users_to_csv


class TestDataParser(unittest.TestCase):

    def test_parse_users(self):

        users = [
            {
                "id": 1,
                "name": "Pranav",
                "username": "pranav",
                "email": "pranav@example.com",
                "address": {"city": "Raigarh"},
                "company": {"name": "Test Company"}
            }
        ]

        dataframe = parse_users(users)

        self.assertEqual(len(dataframe), 1)
        self.assertEqual(dataframe.loc[0, "name"], "Pranav")
        self.assertEqual(dataframe.loc[0, "city"], "Raigarh")


    def test_empty_users(self):

        dataframe = parse_users([])

        self.assertTrue(dataframe.empty)


    def test_invalid_input(self):

        with self.assertRaises(TypeError):
            parse_users({"id": 1})


    def test_save_users_to_csv(self):

        dataframe = parse_users([
            {"id": 1, "name": "Pranav"}
        ])

        with tempfile.TemporaryDirectory() as folder:

            output_file = Path(folder) / "users.csv"

            save_users_to_csv(dataframe, output_file)

            self.assertTrue(output_file.exists())


if __name__ == "__main__":
    unittest.main()