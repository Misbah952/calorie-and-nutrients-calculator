import unittest
import os
import csv
from signupwindow import SignUpWindow  # Import the class containing the confirm_sign_up function


class TestAddNewUser(unittest.TestCase):
    def setUp(self):
        # Create a temporary test directory for user data
        self.test_user_dir = "test_users"
        os.makedirs(self.test_user_dir)

    def test_confirm_sign_up(self):
        # Define test data
        test_data = [
            {"first_name": "John", "last_name": "Doe", "pincode": "1234"},
            {"first_name": "Alice", "last_name": "Smith", "pincode": "5678"},

        ]

        # Loop through each test data
        for data in test_data:
            # Simulate user input
            first_name = data["first_name"]
            last_name = data["last_name"]
            pincode = data["pincode"]

            # Call the function to be tested
            sign_up_window = SignUpWindow()
            sign_up_window.first_name_edit.setText(first_name)
            sign_up_window.last_name_edit.setText(last_name)
            sign_up_window.pincode_edit.setText(pincode)
            sign_up_window.confirm_sign_up()

            # Verify if the new user is added to user_credentials.csv
            user_credentials_file = "user_credentials.csv"
            with open(user_credentials_file, "r") as csvfile:
                reader = csv.reader(csvfile)
                user_credentials = list(reader)
                new_user_credentials = [first_name[0].upper() + last_name.capitalize(), pincode]
                self.assertIn(new_user_credentials, user_credentials)

            # Verify if the corresponding user directory is created
            user_directory = f"{self.test_user_dir}/{first_name[0].upper() + last_name.capitalize()}"
            self.assertTrue(os.path.exists(user_directory))

            # Verify if username.csv file is created
            username_file = f"{user_directory}/{first_name[0].upper() + last_name.capitalize()}.csv"
            self.assertTrue(os.path.exists(username_file))

            # Verify if username_mealdata.csv file is created
            mealdata_file = f"{user_directory}/{first_name[0].upper() + last_name.capitalize()}_mealdata.csv"
            self.assertTrue(os.path.exists(mealdata_file))
