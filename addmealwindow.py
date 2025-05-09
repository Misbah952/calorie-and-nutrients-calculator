from PyQt6.QtWidgets import QDialog, QPushButton, QVBoxLayout, QLineEdit, QLabel, QMessageBox, QInputDialog
from PyQt6.QtGui import QImage, QPalette, QBrush
from PyQt6.QtCore import Qt
import datetime
import csv
import os


class AddMealWindow(QDialog):
    def __init__(self, username):
        super().__init__()

        self.setWindowTitle("Add Meal")
        self.setGeometry(100, 100, 400, 200)

        self.username = username

        # Background image
        background_image = QImage("Image1.jpg")
        blurred_image = background_image.scaled(self.size(), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding, transformMode=Qt.TransformationMode.SmoothTransformation)

        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(blurred_image))
        self.setPalette(palette)

        layout = QVBoxLayout()

        # Date input
        self.date_edit = QLineEdit()
        layout.addWidget(QLabel("Enter Date (YYYY-MM-DD):"))
        layout.addWidget(self.date_edit)

        # Buttons for meal types
        meal_types_layout = QVBoxLayout()
        self.meal_buttons = {}
        for meal_type in ["Breakfast", "Snack", "Lunch", "Dinner"]:
            button = QPushButton(meal_type)
            button.clicked.connect(lambda _, m=meal_type: self.add_meal(m))
            meal_types_layout.addWidget(button)
            self.meal_buttons[meal_type] = button
        layout.addLayout(meal_types_layout)

        self.setLayout(layout)

    def add_meal(self, meal_type):
        # Get the input date
        date = self.date_edit.text()

        # Validate date format
        if not self.is_valid_date_format(date):
            QMessageBox.warning(self, "Error", "Invalid date format. Please enter date in YYYY-MM-DD format.")
            return

        # Ask user to input meal details
        (protein, carbohydrates, fats, vitamin_a, vitamin_b, vitamin_c, vitamin_d, dietary_fibre, magnesium, iron,
         calcium) = self.get_meal_details()

        # Calculate total calories
        total_calories = (4 * (
                    protein + carbohydrates) + 9 * fats + vitamin_a + vitamin_b + vitamin_c + vitamin_d + dietary_fibre
                          + magnesium + iron + calcium)

        # add meal to username_mealdata.csv
        try:
            meal_data = [date, meal_type, protein, carbohydrates, fats, vitamin_a, vitamin_b,
                         vitamin_c, vitamin_d, dietary_fibre, magnesium, iron, calcium, total_calories, 0, 0, 0, 0, 0]
            user_mealdata_path = os.path.join("users", self.username, f"{self.username}_mealdata.csv")
            with open(user_mealdata_path, "a", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(meal_data)
            QMessageBox.information(self, "Success", f"Meal added successfully!\nDate: {date}\nMeal Type: {meal_type}")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"An error occurred: {str(e)}")

    def get_meal_details(self):
        protein = float(QInputDialog.getText(self, "Enter Protein", "Protein (g):")[0])
        carbohydrates = float(QInputDialog.getText(self, "Enter Carbohydrates", "Carbohydrates (g):")[0])
        fats = float(QInputDialog.getText(self, "Enter Fats", "Fats (g):")[0])
        vitamin_a = float(QInputDialog.getText(self, "Enter Vitamin A", "Vitamin A (IU):")[0])
        vitamin_b = float(QInputDialog.getText(self, "Enter Vitamin B", "Vitamin B (mg):")[0])
        vitamin_c = float(QInputDialog.getText(self, "Enter Vitamin C", "Vitamin C (mg):")[0])
        vitamin_d = float(QInputDialog.getText(self, "Enter Vitamin D", "Vitamin D (IU):")[0])
        dietary_fibre = float(QInputDialog.getText(self, "Enter Dietary Fibre", "Dietary Fibre (g):")[0])
        magnesium = float(QInputDialog.getText(self, "Enter Magnesium", "Magnesium (mg):")[0])
        iron = float(QInputDialog.getText(self, "Enter Iron", "Iron (mg):")[0])
        calcium = float(QInputDialog.getText(self, "Enter Calcium", "Calcium (mg):")[0])

        return (protein, carbohydrates, fats, vitamin_a, vitamin_b, vitamin_c,
                vitamin_d, dietary_fibre, magnesium, iron, calcium)

    @staticmethod
    def is_valid_date_format(date):
        try:
            # Attempt to parse the date
            _ = datetime.datetime.strptime(date, '%Y-%m-%d')
            return True
        except ValueError:
            return False
