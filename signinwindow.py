from PyQt6.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout, QLabel, QMessageBox
from PyQt6.QtGui import QImage, QPalette, QBrush
from PyQt6.QtCore import Qt
from userdashboard import UserDashboard
import csv


class SignInWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sign In")
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

        self.username_edit = QLineEdit()
        self.pincode_edit = QLineEdit()
        self.pincode_edit.setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.username_edit)
        layout.addWidget(QLabel("Pin Code:"))
        layout.addWidget(self.pincode_edit)

        confirm_button = QPushButton("Sign In")
        confirm_button.clicked.connect(self.confirm_sign_in)
        layout.addWidget(confirm_button)

        self.setLayout(layout)

    def confirm_sign_in(self):
        username = self.username_edit.text()
        pincode = self.pincode_edit.text()

        if username and pincode:
            try:
                # Read the CSV file to check if the username and pincode match
                with open("user_credentials.csv", "r") as csvfile:
                    reader = csv.reader(csvfile)
                    next(reader)  # Skip the header row
                    for row in reader:
                        print("Row:", row)  # Debug print statement
                        if row[0] == username and row[1] == pincode:
                            QMessageBox.information(self, "Success", "Sign in successful!")
                            self.user_dashboard = UserDashboard(username)
                            self.user_dashboard.show()
                            self.close()  # Close the sign-in window after successful sign-in
                            return
                    QMessageBox.warning(self, "Error", "Incorrect username or pincode.")
            except Exception as e:
                print("Error:", e)  # Debug print statement
                QMessageBox.warning(self, "Error", "An error occurred while reading user credentials.")
        else:
            QMessageBox.warning(self, "Error", "Please fill in all fields.")
