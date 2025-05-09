from PyQt6.QtCore import Qt
from PyQt6.QtGui import QImage, QPalette, QBrush
from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget

from addmealwindow import AddMealWindow
from changepincode import ChangePincode
from updateprofilewindow import UpdateProfileWindow
from viewannualcalorieconsumption import ViewAnnualCalorieConsumption
from viewbmiwindow import ViewBMIWindow
from viewdailycalorieconsumption import ViewDailyCalorieConsumption
from viewmonthlycalorieconsumption import ViewMonthlyCalorieConsumption


class UserDashboard(QMainWindow):
    def __init__(self, username):
        super().__init__()

        self.setWindowTitle("User Dashboard")
        self.setGeometry(100, 100, 800, 600)
        self.username = username

        # Background image
        background_image = QImage("Image2.jpg")
        blurred_image = background_image.scaled(
            self.size(),
            aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            transformMode=Qt.TransformationMode.SmoothTransformation
        )

        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(blurred_image))
        self.setPalette(palette)

        layout = QVBoxLayout()
        central_widget = QWidget()

        update_profile_button = QPushButton("Update Profile")  # Button to update profile
        update_profile_button.clicked.connect(self.open_update_profile_window)
        layout.addWidget(update_profile_button)

        view_bmi_button = QPushButton("View BMI Status")     # button to view BMI status
        view_bmi_button.clicked.connect(self.open_view_bmi_window)
        layout.addWidget(view_bmi_button)

        add_meal_button = QPushButton("Add Meal")           # Button to Add Meal
        add_meal_button.clicked.connect(self.open_add_meal_window)
        layout.addWidget(add_meal_button)

        view_daily_calorie_consumption_button = QPushButton("View Daily Calorie Consumption")  # Button to view daily calorie consumption
        view_daily_calorie_consumption_button.clicked.connect(self.view_daily_calorie_consumption)  # Connect to method
        layout.addWidget(view_daily_calorie_consumption_button)

        view_monthly_calorie_consumption_button = QPushButton("View Monthly Calorie Consumption") # Button to view Monthly calorie consumption
        view_monthly_calorie_consumption_button.clicked.connect(self.view_monthly_calorie_consumption)
        layout.addWidget(view_monthly_calorie_consumption_button)

        view_annual_calorie_consumption_button = QPushButton("View Annual Calorie Consumption") # Button to view Annual calorie consumption
        view_annual_calorie_consumption_button.clicked.connect(self.view_annual_calorie_consumption)
        layout.addWidget(view_annual_calorie_consumption_button)

        change_pincode_button = QPushButton("Change Pincode") # Button to change pincode
        change_pincode_button.clicked.connect(self.change_pincode)
        layout.addWidget(change_pincode_button)

        Signout_button = QPushButton("Sign Out") # Button to Signout
        Signout_button.clicked.connect(self.signout)
        layout.addWidget(Signout_button)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_update_profile_window(self):
        self.update_profile_window = UpdateProfileWindow(username=self.username)
        self.update_profile_window.show()

    def open_view_bmi_window(self):
        self.view_bmi_window = ViewBMIWindow(username=self.username)
        self.view_bmi_window.show()

    def open_add_meal_window(self):
        self.add_meal_window = AddMealWindow(username=self.username)
        self.add_meal_window.show()

    def view_daily_calorie_consumption(self):
        self.view_daily_calorie_consumption = ViewDailyCalorieConsumption(username=self.username)
        self.view_daily_calorie_consumption.show()

    def view_monthly_calorie_consumption(self):
        self.view_monthly_calorie_consumption = ViewMonthlyCalorieConsumption(username=self.username)
        self.view_monthly_calorie_consumption.show()

    def view_annual_calorie_consumption(self):
        self.view_annual_calorie_consumption = ViewAnnualCalorieConsumption(username=self.username)
        self.view_annual_calorie_consumption.show()

    def change_pincode(self):
        self.change_pincode = ChangePincode(username=self.username)
        self.change_pincode.show()

    def signout(self):
        self.close()
