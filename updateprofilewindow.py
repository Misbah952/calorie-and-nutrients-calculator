from PyQt6.QtWidgets import QDialog, QPushButton, QVBoxLayout, QLabel, QLineEdit, QMessageBox
from PyQt6.QtGui import QImage, QPalette, QBrush
from PyQt6.QtCore import pyqtSlot, Qt
import csv
import os


class UpdateProfileWindow(QDialog):
    def __init__(self, username):
        super().__init__()

        self.setWindowTitle("Update Profile")
        self.setGeometry(100, 100, 300, 200)
        self.username = username

        # Background image
        background_image = QImage("egg.jpg")
        blurred_image = background_image.scaled(self.size(), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding, transformMode=Qt.TransformationMode.SmoothTransformation)

        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(blurred_image))
        self.setPalette(palette)

        layout = QVBoxLayout()

        # Widgets for updating weight
        self.weight_edit = QLineEdit()
        layout.addWidget(QLabel("Enter Weight (kg):"))
        layout.addWidget(self.weight_edit)
        update_weight_button = QPushButton("Update Weight")
        update_weight_button.clicked.connect(lambda: self.update_profile_detail("Weight", self.weight_edit.text()))
        layout.addWidget(update_weight_button)

        # Widgets for updating height
        self.height_edit = QLineEdit()
        layout.addWidget(QLabel("Enter Height (cm):"))
        layout.addWidget(self.height_edit)
        update_height_button = QPushButton("Update Height")
        update_height_button.clicked.connect(lambda: self.update_profile_detail("Height", self.height_edit.text()))
        layout.addWidget(update_height_button)



        # Widgets for updating daily calorie limit
        self.daily_calorie_limit_edit = QLineEdit()
        layout.addWidget(QLabel("Enter Daily Calorie Limit:"))
        layout.addWidget(self.daily_calorie_limit_edit)
        update_daily_calorie_limit_button = QPushButton("Update Daily Calorie Limit")
        update_daily_calorie_limit_button.clicked.connect(lambda: self.update_profile_detail("Daily Calorie Limit", self.daily_calorie_limit_edit.text()))
        layout.addWidget(update_daily_calorie_limit_button)

        # Widgets for updating monthly calorie limit
        self.monthly_calorie_limit_edit = QLineEdit()
        layout.addWidget(QLabel("Enter Monthly Calorie Limit:"))
        layout.addWidget(self.monthly_calorie_limit_edit)
        update_monthly_calorie_limit_button = QPushButton("Update Monthly Calorie Limit")
        update_monthly_calorie_limit_button.clicked.connect(lambda: self.update_profile_detail("Monthly Calorie Limit", self.monthly_calorie_limit_edit.text()))
        layout.addWidget(update_monthly_calorie_limit_button)

        # Widgets for updating annual calorie limit
        self.annual_calorie_limit_edit = QLineEdit()
        layout.addWidget(QLabel("Enter Annual Calorie Limit:"))
        layout.addWidget(self.annual_calorie_limit_edit)
        update_annual_calorie_limit_button = QPushButton("Update Annual Calorie Limit")
        update_annual_calorie_limit_button.clicked.connect(lambda: self.update_profile_detail("Annual Calorie Limit", self.annual_calorie_limit_edit.text()))
        layout.addWidget(update_annual_calorie_limit_button)

        self.setLayout(layout)

    @pyqtSlot()
    def update_profile_detail(self, field, value):
        if value:
            try:
                # Read the existing data from the username.csv file
                user_file_path = os.path.join("users", self.username, f"{self.username}.csv")

                with open(user_file_path, "r") as user_file:
                    reader = csv.reader(user_file)
                    data = list(reader)

                # Find the index of the field in the header row
                header_row = data[0]
                if field not in header_row:
                    raise ValueError(f"{field} not found in the header row.")

                field_index = header_row.index(field)

                # Update the value
                data[1][field_index] = value  #  data starts from the second row

                # Write the updated data back to the file
                with open(user_file_path, "w", newline="") as user_file:
                    writer = csv.writer(user_file)
                    writer.writerows(data)

                QMessageBox.information(self, "Success", f"{field} updated successfully!")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"An error occurred: {str(e)}")
        else:
            QMessageBox.warning(self, "Error", f"Please enter the {field.lower()}.")


