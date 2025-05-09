# Nutrients and Calorie Calculator

This application allows users to track their daily, monthly, and annual calorie consumption, manage their profile details, and analyze nutrient percentages through a graphical user interface (GUI) built with PyQt6.

---

## Class Descriptions

| **Class Name**                  | **Description** |
|---------------------------------|-----------------|
| `MainWindow`                    | Represents the main window. Provides a welcome screen and options to sign up or sign in. |
| `SignUpWindow`                  | Allows new users to register with first name, last name, and pin code. Generates a username upon successful signup. |
| `TestGenerateUsername`          | Unit test class for verifying username generation. |
| `TestAddNewUser`                | Unit test class for verifying the addition of new users to the system. |
| `SignInWindow`                  | Allows users to log in using their username and pin code. |
| `UserDashboard`                 | Interface for users to add meals, view calories, and update profile details. |
| `UpdateProfileWindow`           | Allows updates to profile data such as height, weight, and calorie limits. |
| `ViewBMI`                       | Displays Body Mass Index (BMI) and corresponding status. |
| `AddMealWindow`                 | Allows entry of meal details (breakfast, lunch, dinner, snack). |
| `ViewDailyCalorieConsumption`   | Displays calories consumed on a selected day. |
| `ViewMonthlyCalorieConsumption` | Shows monthly calorie consumption using pie charts. |
| `ViewAnnualCalorieConsumption`  | Displays total calorie consumption over a year. |
| `ChangePincode`                 | Enables users to change their account PIN. |
| `Utility`                       | Contains utility functions like `generate_username` and `draw_pie_chart`. |

---


## Libraries Used

- **PyQt6**: For GUI creation and user interaction.
- **CSV**: For handling user profile and meal data storage.
- **OS**: For file path and directory access.
- **datetime**: For date input validation and processing.

---

## Features

- PIN code protection
- Change password functionality
- Each user has two CSV files: one for profile data, one for meal data
- View:
  - Daily calories consumed
  - Monthly calories consumed
  - Annual calories consumed
  - BMI
- Select meal type (breakfast, snack, lunch, dinner)
- View nutrient consumption percentages
- Set daily, monthly, and annual calorie limits

## How to Run This Project

1. **Install dependencies**  
   Ensure you have Python 3.9+ installed. Then, install the required libraries:

   ```bash
   pip install pyqt6

   git clone <repository_url>
   cd <project_directory>

   python main.py
