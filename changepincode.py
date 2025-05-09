from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt6.QtGui import QImage, QPalette, QBrush
from PyQt6.QtCore import Qt
import csv
class ChangePincode(QDialog):
    def __init__(self, username):
        super().__init__()

        self.setWindowTitle("Change Pincode")
        self.setGeometry(100, 100, 400, 200)

        # Background image
        background_image = QImage("Image1.jpg")
        blurred_image = background_image.scaled(self.size(),
                                                aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                                                transformMode=Qt.TransformationMode.SmoothTransformation)

        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(blurred_image))
        self.setPalette(palette)

        layout = QVBoxLayout()

        self.pincode_edit = QLineEdit()
        layout.addWidget(QLabel("Enter New Pincode (or leave empty to keep current pincode):"))
        layout.addWidget(self.pincode_edit)

        update_button = QPushButton("Update")
        update_button.clicked.connect(self.update_pincode)
        layout.addWidget(update_button)

        self.setLayout(layout)

        self.username = username

    def update_pincode(self):
        new_pincode = self.pincode_edit.text()
        try:
            # Read existing data from user_credentials.csv
            credentials_path = "user_credentials.csv"
            with open(credentials_path, "r") as credentials_file:
                reader = csv.DictReader(credentials_file)
                credentials = list(reader)

            # Update the pincode
            for cred in credentials:
                if cred["Username"] == self.username:
                    if new_pincode:
                        cred["Pincode"] = new_pincode

            # Write updated data back to user_credentials.csv
            with open(credentials_path, "w", newline="") as credentials_file:
                fieldnames = ["Username", "Pincode"]
                writer = csv.DictWriter(credentials_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(credentials)

            QMessageBox.information(self, "Success", "Pincode updated successfully!")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"An error occurred: {str(e)}")
