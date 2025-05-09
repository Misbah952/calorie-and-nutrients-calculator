import unittest
from utility import generate_username

class TestGenerateUsername(unittest.TestCase):
    def test_generate_username(self):

        # Test case 1: Both first name and last name provided
        username_1 = generate_username("John", "Doe")
        self.assertEqual(username_1, "JDoe")

        # Test case 2: First name only
        username_2 = generate_username("Alice", "")
        self.assertIsNone(username_2, "A")

        # Test case 3: Last name only
        username_3 = generate_username("", "Smith")
        self.assertIsNone(username_3, "Smith")

        # Test case 4: Empty first name and last name
        username_4 = generate_username("", "")
        self.assertIsNone(username_4, "")


