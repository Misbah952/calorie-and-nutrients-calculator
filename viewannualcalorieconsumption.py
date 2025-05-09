import os
import csv
from PyQt6.QtGui import QImage, QPalette, QBrush
from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QGraphicsScene, \
    QGraphicsView
from PyQt6.QtCore import Qt
from utility import drawPieChart

class ViewAnnualCalorieConsumption(QDialog):
    def __init__(self, username):
        super().__init__()

        self.setWindowTitle("View Annual Calorie Consumption")
        self.setGeometry(100, 100, 400, 200)

        # Background image
        background_image = QImage("Image2.jpg")
        blurred_image = background_image.scaled(self.size(), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding, transformMode=Qt.TransformationMode.SmoothTransformation)

        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(blurred_image))
        self.setPalette(palette)

        layout = QVBoxLayout()

        self.year_edit = QLineEdit()
        layout.addWidget(QLabel("Enter Year (YYYY):"))
        layout.addWidget(self.year_edit)

        view_button = QPushButton("View")
        view_button.clicked.connect(self.view_annual_calorie_consumption)
        layout.addWidget(view_button)

        chart_button = QPushButton("View PieChart")
        chart_button.clicked.connect(self.view_piechart)
        layout.addWidget(chart_button)

        self.setLayout(layout)

        self.username = username

    def view_annual_calorie_consumption(self):
        year = self.year_edit.text()
        if year:
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
                        if row["Date"].startswith(year):
                            for nutrient, value in nutrient_totals.items():
                                nutrient_totals[nutrient] += float(row[nutrient])

                    # Calculate consumed calories
                    consumed_calories = 4 * nutrient_totals["Protein"] + 4 * nutrient_totals["Carbohydrates"] + \
                                        9 * nutrient_totals["Fats"] + nutrient_totals["Vitamin A"] + \
                                        nutrient_totals["Vitamin B"] + nutrient_totals["Vitamin C"] + \
                                        nutrient_totals["Vitamin D"] + nutrient_totals["Dietary Fibre"] + \
                                        nutrient_totals["Magnesium"] + nutrient_totals["Iron"] + nutrient_totals["Calcium"]

                # Read annual calorie limit from username.csv
                with open(user_info_path, "r") as user_file:
                    reader = csv.DictReader(user_file)
                    for row in reader:
                        annual_calorie_limit = float(row["Annual Calorie Limit"])

                remaining_calories = annual_calorie_limit - consumed_calories
                if remaining_calories >= 0:
                    status = "Under the limit"
                else:
                    status = "Over the limit"

                # Calculate percentage of each nutrient consumed
                nutrient_percentages = {nutrient: (nutrient_totals[nutrient] / consumed_calories) * 100 if consumed_calories > 0 else 0
                                        for nutrient in nutrient_totals}

                # Display the results
                message = f"Year: {year}\n"
                message += f"Total Consumed Calories: {consumed_calories}\n"
                message += f"Remaining Calories: {remaining_calories}\n"
                message += f"Status: {status}\n"
                message += "Nutrient Percentages:\n"
                for nutrient, percentage in nutrient_percentages.items():
                    message += f"{nutrient}: {percentage:.2f}%\n"

                QMessageBox.information(self, "Annual Calorie Consumption", message)

            except Exception as e:
                QMessageBox.warning(self, "Error", f"An error occurred: {str(e)}")
        else:
            QMessageBox.warning(self, "Error", "Please enter the year.")

    def view_piechart(self):
        year = self.year_edit.text()
        if year:
            try:
                # Construct file path based on the username
                user_mealdata_path = os.path.join("users", self.username, f"{self.username}_mealdata.csv")

                # Read the data from user_mealdata.csv for the given year
                nutrient_totals = {"Protein": 0, "Carbohydrates": 0, "Fats": 0, "Vitamin A": 0,
                                   "Vitamin B": 0, "Vitamin C": 0, "Vitamin D": 0, "Dietary Fibre": 0,
                                   "Magnesium": 0, "Iron": 0, "Calcium": 0}
                with open(user_mealdata_path, "r") as mealdata_file:
                    reader = csv.DictReader(mealdata_file)
                    for row in reader:
                        if row["Date"].startswith(year):
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
            QMessageBox.warning(self, "Error", "Please enter the year.")