## Calorie And Nutrients Calculator

This application allows users to track their daily, monthly, annual calorie consumption, manage their profile details, and analyze nutrient percentages through a graphical user interface (GUI) built with PyQt6.

## Employee Information

| Class                                 |  Breif Description                                |
|---------------------------------------|---------------------------------------------------|
| MainWindow                            | This class represents the main window of the      |
                                          Nutrients and Calorie Calculator application. It  |
                                          provides a welcome screen to the users and        |
                                          options to sign up or sign in.                    |
| SignUpWindow                          |                                                   | 
| TestGenerateUsername                  |                                                   |
| TestAddNewUser                        |                                                   |
| SignInWindow                          |                                                   |
| UserDashboard                         |                                                   |
| UpdateProfileWindow                   |                                                   |
| ViewBMI                               |                                                   |
| AddMealWindow                         |                                                   |
| ViewDailyCalorieConsumption           |                                                   |
| ViewAnnualCalorieConsumption          |                                                   |
| ViewMonthlyCalorieConsumption         |                                                   |
| ChangePincode                         |                                                   |
| Utility                               |                                                   |  



# Nutrients and Calorie Calculator

This application allows users to track their daily, monthly, and annual calorie consumption, manage their profile details, and analyze nutrient percentages through a graphical user interface (GUI) built with PyQt6.

---

## Class Brief Description

- **MainWindow**  
  Represents the main window of the application. Provides a welcome screen and options to sign up or sign in.

- **SignUpWindow**  
  Allows new users to register by entering their first name, last name, and pin code. Generates a username upon successful signup.

- **TestGenerateUsername**  
  Unit test class for testing the username generation functionality.

- **TestAddNewUser**  
  Unit test class for verifying the addition of new users to the system.

- **SignInWindow**  
  Enables registered users to log in using their username and pin code.

- **UserDashboard**  
  Interface for registered users with functionalities like adding meals, viewing consumed calories, and updating profile details.

- **UpdateProfileWindow**  
  Allows users to update profile information such as height, weight, and calorie limits.

- **ViewBMI**  
  Displays the user's Body Mass Index (BMI) and corresponding status based on profile data.

- **AddMealWindow**  
  Allows users to input meal details, including type (e.g., breakfast, lunch, dinner, snack).

- **ViewDailyCalorieConsumption**  
  Displays the daily calorie consumption and meal details for a specific day.

- **ViewMonthlyCalorieConsumption**  
  Shows monthly calorie consumption in a pie chart format.

- **ViewAnnualCalorieConsumption**  
  Displays total annual calorie consumption.

- **ChangePincode**  
  Allows users to change their PIN for account security.

- **Utility**  
  Contains static utility methods such as:
  - `generate_username`: Generates usernames from user details.
  - `draw_pie_chart`: Draws pie charts for nutrient consumption visualization.

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
