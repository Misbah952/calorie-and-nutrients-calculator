Nutrients and Calorie Calculator
This application allows users to track their daily, monthly, and annual calorie consumption, manage their profile details, and analyze nutrient percentages through a graphical user interface (GUI) built with PyQt6.
Classes:
MainWindow: Displays the main dashboard for users to navigate through various features.
SigninWindow: Allows users to Signup, requires Firstname, lastname and pincode. Generates a uername
SigninWindow: Allows Signin using a username and pincode
Userdashboard: Gives user different options to select such a add meal, view calories. update details.
UpdateProfileWindow: Allows users to update their profile details such as weight, height, pincode, and calorie limits.
ChangePincodeWindow: Enables users to change their pincode.
AddMealWindow: Enables users to add meals with nutritional details, updating the meal data CSV.
ViewDailyCalorieConsumption: Displays the total consumed and remaining calories for a specific date.
ViewMonthlyCalorieConsumption: Displays the total consumed and remaining calories for a specific month.
ViewAnnualCalorieConsumption: Displays the total consumed and remaining calories for a specific year.
Libraries:
PyQt6: For building the graphical user interface (GUI) and handling user interactions.
csv: For reading and writing CSV files to manage user profile data and meal information.
os: For accessing file paths and directories within the operating system.
datetime: For validating and processing date inputs in the meal data.
What exactly is used from PyQT?
QDialog: Used for creating dialog windows, which are typically used for modal pop-up windows or custom dialogs.
QPushButton: Represents a clickable button widget that users can interact with.
QVBoxLayout: Arranges widgets vertically in a layout, making it easier to organize the user interface components.
QLabel: Displays text or an image and provides various features for customizing its appearance.
QLineEdit: Allows users to enter and edit a single line of plain text.
QMessageBox: Provides a modal dialog for informing the user or for asking the user a question and receiving an answer.
QHBoxLayout: Arranges widgets horizontally in a layout, similar to QVBoxLayout but aligns widgets side by side horizontally.
QApplication: Represents the application itself and is necessary for running the PyQt6 application.
QPixmap: This class is used for working with images in PyQt6. It allows loading, scaling, and displaying image data from files, resources, or raw pixel data.
Qt: This module provides various Qt-related functionalities and constants. In the context of PyQt6, it includes flags, enums, and constants used for specifying alignment, event handling, and other properties related to Qt widgets and applications.
Features:
Pincode Protection
User can change password
Every user has a two csv files. One for profile data and other for saving the calories consumed for each meal
View Daily calories consumed
View Monthly Calories consumed
View annual calories consumed
View BMI
user can select the type of meal such as breakfast, snack, lunch or dinner
User can view percentages of the nutrients consumed.
User can set daily calorie limit
User can set monthly calorie limit
User can set annual calorie limit