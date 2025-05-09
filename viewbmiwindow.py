from PyQt6.QtGui import QImage, QPalette, QBrush
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
import csv
import os

class ViewBMIWindow(QDialog):
    def __init__(self, username):
        super().__init__()

        self.setWindowTitle("View BMI Status")
        self.setGeometry(100, 100, 400, 300)

        self.username = username

        # Background image
        background_image = QImage("bmi.jpg")
        blurred_image = background_image.scaled(self.size(), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding, transformMode=Qt.TransformationMode.SmoothTransformation)

        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(blurred_image))
        self.setPalette(palette)

        layout = QVBoxLayout()

        # Read weight and height from username.csv
        weight, height = self.get_weight_and_height_from_csv()

        if weight is not None and height is not None:
            # Calculate BMI
            bmi_value = self.calculate_bmi(weight, height)

            # Determine BMI status and get motivational quote
            bmi_status, motivational_quote = self.get_bmi_status_and_quote(bmi_value)

            # Display BMI information
            layout.addWidget(QLabel(f"Username: {self.username}"))
            layout.addWidget(QLabel(f"Weight: {weight} kg"))
            layout.addWidget(QLabel(f"Height: {height} cm"))
            layout.addWidget(QLabel(f"BMI Value: {bmi_value:.2f}"))
            layout.addWidget(QLabel(f"BMI Status: {bmi_status}"))
            layout.addWidget(QLabel(f"Motivational Quote: {motivational_quote}"))

            # Write BMI value back to username.csv
            self.write_bmi_to_csv(bmi_value)
        else:
            layout.addWidget(QLabel("Failed to retrieve weight and height data."))

        self.setLayout(layout)

    def get_weight_and_height_from_csv(self):
        user_file_path = os.path.join("users", self.username, f"{self.username}.csv")
        try:
            with open(user_file_path, "r") as user_file:
                reader = csv.reader(user_file)
                next(reader)  # Skip header row
                for row in reader:
                    weight = float(row[3])  # weight is in the 4th column (0-based index)
                    height = float(row[4])  # height is in the 5th column (0-based index)
                    return weight, height
        except Exception as e:
            print("Error reading username.csv:", e)
            return None, None

    @staticmethod
    def calculate_bmi(weight, height):
        # BMI formula: BMI = weight(kg) / (height(m) * height(m))
        height_in_meters = height / 100  # Convert height from cm to meters
        return weight / (height_in_meters * height_in_meters)

    @staticmethod
    def get_bmi_status_and_quote(bmi_value):
        # Determines BMI status and get motivational quote based on the BMI value
        if bmi_value < 18.5:
            return "Underweight", (
                "You are braver than you believe, stronger than you seem, "
                "and smarter than you think. - A.A. Milne"
            )
        elif 18.5 <= bmi_value < 25:
            return "Normal weight", "The only bad workout is the one that didn't happen."
        elif 25 <= bmi_value < 30:
            return "Overweight", "Success is the sum of small efforts, repeated day-in and day-out."
        else:
            return "Obese", "You don't have to be great to start, but you have to start to be great. - Zig Ziglar"

    def write_bmi_to_csv(self, bmi_value):
        try:
            user_file_path = os.path.join("users", self.username, f"{self.username}.csv")
            with open(user_file_path, "r") as user_file:
                reader = csv.reader(user_file)
                rows = list(reader)
                header = rows[0]  # Gets the header row
                data = rows[1:]  # Skips the header row

            # Finds the index of the BMI column
            bmi_index = header.index("BMI")

            # Updates the BMI value in the data
            for row in data:
                row[bmi_index] = f"{bmi_value:.2f}"

            # Writes the updated data back to the CSV file
            with open(user_file_path, "w", newline="") as user_file:
                writer = csv.writer(user_file)
                writer.writerow(header)  # Writes the header row
                writer.writerows(data)  # Writes the updated data
        except Exception as e:
            print("Error writing BMI to username.csv:", e)
