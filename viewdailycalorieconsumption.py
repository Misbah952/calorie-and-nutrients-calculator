import csv
import os

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QImage, QPalette, QBrush
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QDialog, QLabel, QLineEdit, \
    QMessageBox, QGraphicsScene, QGraphicsView

from utility import drawPieChart


class ViewDailyCalorieConsumption(QDialog):
    def __init__(self, username):
        super().__init__()

        self.setWindowTitle("View Daily Calorie Consumption")
        self.setGeometry(100, 100, 400, 200)

        # Background image
        background_image = QImage("Image2.jpg")
        blurred_image = background_image.scaled(self.size(),
                                                aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                                                transformMode=Qt.TransformationMode.SmoothTransformation)

        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(blurred_image))
        self.setPalette(palette)

        layout = QVBoxLayout()

        self.date_edit = QLineEdit()
        layout.addWidget(QLabel("Enter Date (YYYY-MM-DD):"))
        layout.addWidget(self.date_edit)

        view_button = QPushButton("View Consumption")
        view_button.clicked.connect(self.view_daily_calorie_consumption)
        layout.addWidget(view_button)

        nutrients_button = QPushButton("View Nutrients Details")
        nutrients_button.clicked.connect(self.view_nutrients_details)
        layout.addWidget(nutrients_button)

        chart_button = QPushButton("View PieChart")
        chart_button.clicked.connect(self.view_piechart)
        layout.addWidget(chart_button)

        self.setLayout(layout)

        self.username = username

    def view_daily_calorie_consumption(self):
        date = self.date_edit.text()
        if date:
            try:
                # Construct file paths based on the username
                user_mealdata_path = os.path.join("users", self.username, f"{self.username}_mealdata.csv")
                user_info_path = os.path.join("users", self.username, f"{self.username}.csv")

                # Read the data from user_mealdata.csv
                with open(user_mealdata_path, "r") as mealdata_file:
                    reader = csv.DictReader(mealdata_file)
                    consumed_calories = 0
                    nutrient_totals = {"Protein": 0, "Carbohydrates": 0, "Fats": 0, "Vitamin A": 0,
                                       "Vitamin B": 0, "Vitamin C": 0, "Vitamin D": 0, "Dietary Fibre": 0,
                                       "Magnesium": 0, "Iron": 0, "Calcium": 0}
                    for row in reader:
                        if row["Date"] == date:
                            for nutrient, value in nutrient_totals.items():
                                nutrient_totals[nutrient] += float(row[nutrient])

                    # Calculate consumed calories
                    consumed_calories = 4 * nutrient_totals["Protein"] + 4 * nutrient_totals["Carbohydrates"] + \
                                        9 * nutrient_totals["Fats"] + nutrient_totals["Vitamin A"] + \
                                        nutrient_totals["Vitamin B"] + nutrient_totals["Vitamin C"] + \
                                        nutrient_totals["Vitamin D"] + nutrient_totals["Dietary Fibre"] + \
                                        nutrient_totals["Magnesium"] + nutrient_totals["Iron"] + nutrient_totals[
                                            "Calcium"]

                # Read daily calorie limit from username.csv
                with open(user_info_path, "r") as user_file:
                    reader = csv.DictReader(user_file)
                    for row in reader:
                        daily_calorie_limit = float(row["Daily Calorie Limit"])

                remaining_calories = daily_calorie_limit - consumed_calories
                if remaining_calories >= 0:
                    status = "Under the limit"
                else:
                    status = "Over the limit"

                # Calculate percentage of each nutrient consumed
                nutrient_percentages = {
                    nutrient: (nutrient_totals[nutrient] / consumed_calories) * 100 if consumed_calories > 0 else 0
                    for nutrient in nutrient_totals}

                # Display the results
                message = f"Date: {date}\n"
                message += f"Consumed Calories: {consumed_calories}\n"
                message += f"Remaining Calories: {remaining_calories}\n"
                message += f"Status: {status}\n"
                message += "Nutrient Percentages:\n"
                for nutrient, percentage in nutrient_percentages.items():
                    message += f"{nutrient}: {percentage:.2f}%\n"

                QMessageBox.information(self, "Daily Calorie Consumption", message)

            except Exception as e:
                QMessageBox.warning(self, "Error", f"An error occurred: {str(e)}")
        else:
            QMessageBox.warning(self, "Error", "Please enter the date.")

    def view_nutrients_details(self):
        date = self.date_edit.text()
        if date:
            try:
                # Construct file paths based on the username
                user_mealdata_path = os.path.join("users", self.username, f"{self.username}_mealdata.csv")

                # Read the data from user_mealdata.csv
                with open(user_mealdata_path, "r") as mealdata_file:
                    reader = csv.DictReader(mealdata_file)
                    nutrient_totals = {"Protein": 0, "Carbohydrates": 0, "Fats": 0, "Vitamin A": 0,
                                       "Vitamin B": 0, "Vitamin C": 0, "Vitamin D": 0, "Dietary Fibre": 0,
                                       "Magnesium": 0, "Iron": 0, "Calcium": 0}
                    for row in reader:
                        if row["Date"] == date:
                            for nutrient in nutrient_totals:
                                nutrient_totals[nutrient] += float(row[nutrient])

                # Display the nutrient details
                message = f"Nutrient Details for {date}:\n"
                for nutrient, value in nutrient_totals.items():
                    message += f"{nutrient}: {value} grams\n"

                QMessageBox.information(self, "Nutrient Details", message)

            except Exception as e:
                QMessageBox.warning(self, "Error", f"An error occurred: {str(e)}")
        else:
            QMessageBox.warning(self, "Error", "Please enter the date.")

    def view_piechart(self):
        date = self.date_edit.text()
        if date:
            try:
                # Construct file path based on the username and date
                user_mealdata_path = os.path.join("users", self.username, f"{self.username}_mealdata.csv")

                # Read the data from user_mealdata.csv for the given date
                nutrient_totals = {"Protein": 0, "Carbohydrates": 0, "Fats": 0, "Vitamin A": 0,
                                   "Vitamin B": 0, "Vitamin C": 0, "Vitamin D": 0, "Dietary Fibre": 0,
                                   "Magnesium": 0, "Iron": 0, "Calcium": 0}
                with open(user_mealdata_path, "r") as mealdata_file:
                    reader = csv.DictReader(mealdata_file)
                    for row in reader:
                        if row["Date"] == date:
                            for nutrient in nutrient_totals:
                                nutrient_totals[nutrient] += float(row[nutrient])

                # Display the pie chart
                window = QDialog()
                window.setWindowTitle("Nutrient Consumption Details")
                window.setGeometry(100, 100, 500, 400)

                scene = QGraphicsScene()
                pie_chart_view = QGraphicsView(scene)
                layout = QVBoxLayout()
                layout.addWidget(pie_chart_view)
                window.setLayout(layout)

                drawPieChart(scene, nutrient_totals.values())

                window.exec()

            except Exception as e:
                QMessageBox.warning(self, "Error", f"An error occurred: {str(e)}")
        else:
            QMessageBox.warning(self, "Error", "Please enter the date.")
