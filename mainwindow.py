from PyQt6.QtCore import Qt
from PyQt6.QtGui import QImage, QPalette, QBrush
from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QApplication
from signinwindow import SignInWindow
from signupwindow import SignUpWindow

# This class is for the main where  we have three buttons Signup, Signin and Exit
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nutrients and Calorie Calculator")
        self.setGeometry(100, 100, 800, 600)

        # Background image
        background_image = QImage("MainWindow.jpg")
        blurred_image = background_image.scaled(
            self.size(),
            aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            transformMode=Qt.TransformationMode.SmoothTransformation
        )

        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(blurred_image))
        self.setPalette(palette)

        layout = QVBoxLayout()

        welcome_label = QLabel("Welcome to our Nutrients and Calorie Calculator")
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        welcome_label.setStyleSheet("color: black; font-size: 24px;")

        sign_up_button = QPushButton("Sign Up")
        sign_up_button.clicked.connect(self.open_sign_up_window)

        sign_in_button = QPushButton("Sign In")
        sign_in_button.clicked.connect(self.open_sign_in_window)

        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(QApplication.instance().quit)

        layout.addWidget(welcome_label)
        layout.addWidget(sign_up_button)
        layout.addWidget(sign_in_button)
        layout.addWidget(exit_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_sign_up_window(self):
        self.sign_up_window = SignUpWindow()
        self.sign_up_window.show()

    def open_sign_in_window(self):
        self.sign_in_window = SignInWindow()
        self.sign_in_window.show()
