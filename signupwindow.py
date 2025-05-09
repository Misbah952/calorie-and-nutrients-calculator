from PyQt6.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout, QLabel, QMessageBox
from PyQt6.QtGui import QImage, QPalette, QBrush
from PyQt6.QtCore import Qt
import os
import csv
from utility import generate_username

class SignUpWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sign Up")
        self.setGeometry(100, 100, 300, 200)

        # Background image
        background_image = QImage("SignupWindow.jpg")
        blurred_image = background_image.scaled(self.size(),
                                                aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                                                transformMode=Qt.TransformationMode.SmoothTransformation)

        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(blurred_image))
        self.setPalette(palette)

        layout = QVBoxLayout()

        self.first_name_edit = QLineEdit()
        self.last_name_edit = QLineEdit()
        self.pincode_edit = QLineEdit()

        layout.addWidget(QLabel("First Name:"))
        layout.addWidget(self.first_name_edit)
        layout.addWidget(QLabel("Last Name:"))
        layout.addWidget(self.last_name_edit)
        layout.addWidget(QLabel("Pin Code:"))
        layout.addWidget(self.pincode_edit)

        confirm_button = QPushButton("Sign Up")
        confirm_button.clicked.connect(self.confirm_sign_up)
        layout.addWidget(confirm_button)

        self.setLayout(layout)

    def confirm_sign_up(self):
        first_name = self.first_name_edit.text()
        last_name = self.last_name_edit.text()
        pincode = self.pincode_edit.text()

        if first_name and last_name and pincode:
            # Generate username
            username = generate_username(first_name, last_name)

            # Append username and pincode to user_credentials.csv
            with open("user_credentials.csv", "a", newline="") as csvfile:
                writer = csv.writer(csvfile)
                # Check if the file is empty and write header if it is
                if csvfile.tell() == 0:
                    writer.writerow(["Username", "PinCode"])
                writer.writerow([username, pincode])

            # Create user's directory if it doesn't exist
            user_directory = f"users/{username}"
            if not os.path.exists(user_directory):
                os.makedirs(user_directory)

            # Create username.csv file
            with open(f"{user_directory}/{username}.csv", "w", newline="") as user_file:
                writer = csv.writer(user_file)
                writer.writerow(["First Name", "Last Name", "Username", "Weight", "Height", "BMI",
                                 "Daily Calorie Limit", "Monthly Calorie Limit", "Annual Calorie Limit"])
                writer.writerow([first_name, last_name, username, pincode, 0, 0, 0, 0, 0, 0])

            # Create username_mealdata.csv files
            with open(f"{user_directory}/{username}_mealdata.csv", "w", newline="") as mealdata_file:
                writer = csv.writer(mealdata_file)
                writer.writerow(
                    ["Date", "Meal", "Protein", "Carbohydrates", "Fats", "Vitamin A", "Vitamin B",
                     "Vitamin C", "Vitamin D", "Dietary Fibre", "Magnesium", "Iron", "Calcium",
                     "Calories Consumed"])

            QMessageBox.information(self, "Success",
                                    f"Your sign up was successful. Your username is {username}")
            self.close()  # Close the sign-up window after successful sign-up
        else:
            QMessageBox.warning(self, "Error", "Please fill in all fields.")



