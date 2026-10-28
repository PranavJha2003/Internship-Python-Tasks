
import unittest
from main import clean_value


class TestCleanValue(unittest.TestCase):

    def test_removes_whitespace(self):
        self.assertEqual(clean_value("  North Field  "), "North Field")

    def test_empty_string_returns_none(self):
        self.assertIsNone(clean_value(""))

    def test_missing_value_returns_none(self):
        self.assertIsNone(clean_value(None))


if __name__ == "__main__":
    unittest.main()
