import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QHBoxLayout, QGridLayout, QFrame, QMenuBar, QMainWindow, QMessageBox)
from PyQt6.QtGui import QFont, QAction
from PyQt6.QtCore import Qt


class BMICalculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BMI Calculator")
        self.setGeometry(100, 100, 350, 250)

        # Central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Menu Bar
        menu_bar = self.menuBar()

        # File Menu
        file_menu = menu_bar.addMenu("File")

        clear_action = QAction("Clear", self)
        clear_action.triggered.connect(self.clear_fields)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)

        file_menu.addAction(clear_action)
        file_menu.addAction(exit_action)

        # Help Menu
        help_menu = menu_bar.addMenu("Help")

        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)

        help_menu.addAction(about_action)

        # Title
        title_label = QLabel("BMI Calculator")
        title_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))

        # Input Fields
        self.weight_label = QLabel("Weight:")
        self.weight_input = QLineEdit()
        self.weight_input.setPlaceholderText("kg")

        self.height_label = QLabel("Height:")
        self.height_input = QLineEdit()
        self.height_input.setPlaceholderText("cm")

        # BMI Result Box
        self.bmi_display = QLabel("Your BMI: --")
        self.bmi_display.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.bmi_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bmi_display.setFrameShape(QFrame.Shape.Box)
        self.bmi_display.setStyleSheet("background-color: lightgray; padding: 10px; border-radius: 5px;")

        # Calculate Button
        self.calculate_button = QPushButton("Calculate BMI")
        self.calculate_button.clicked.connect(self.calculate_bmi)

        # BMI Category Labels
        categories_layout = QGridLayout()
        categories = [
            ("Underweight", "< 18.5", "#F4A261"),
            ("Normal weight", "18.5 - 25", "#2A9D8F"),
            ("Overweight", "25 - 30", "#E9C46A"),
            ("Obese", "> 30", "#E76F51")
        ]

        for i, (label, value, color) in enumerate(categories):
            lbl = QLabel(f"{label}\n{value}")
            lbl.setStyleSheet(f"background-color: {color}; padding: 5px; border-radius: 5px; color: white;")
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            categories_layout.addWidget(lbl, 0, i)

        # Layouts
        main_layout = QVBoxLayout()
        grid_layout = QGridLayout()

        grid_layout.addWidget(self.weight_label, 0, 0)
        grid_layout.addWidget(self.weight_input, 0, 1)
        grid_layout.addWidget(self.height_label, 1, 0)
        grid_layout.addWidget(self.height_input, 1, 1)

        main_layout.addWidget(title_label, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addLayout(grid_layout)
        main_layout.addWidget(self.calculate_button)
        main_layout.addWidget(self.bmi_display)
        main_layout.addLayout(categories_layout)

        self.central_widget.setLayout(main_layout)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_input.text())
            height = float(self.height_input.text()) / 100  # Convert cm to meters

            bmi = weight / (height ** 2)
            category, color = self.get_bmi_category(bmi)

            self.bmi_display.setText(f"Your BMI: {bmi:.1f}")
            self.bmi_display.setStyleSheet(
                f"background-color: {color}; padding: 10px; border-radius: 5px; color: white;")
        except ValueError:
            self.bmi_display.setText("Invalid input!")
            self.bmi_display.setStyleSheet("background-color: red; padding: 10px; border-radius: 5px; color: white;")

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight", "#F4A261"
        elif 18.5 <= bmi < 25:
            return "Normal weight", "#2A9D8F"
        elif 25 <= bmi < 30:
            return "Overweight", "#E9C46A"
        else:
            return "Obese", "#E76F51"

    def clear_fields(self):
        """Clears the input fields."""
        self.weight_input.clear()
        self.height_input.clear()
        self.bmi_display.setText("Your BMI: --")
        self.bmi_display.setStyleSheet("background-color: lightgray; padding: 10px; border-radius: 5px;")

    def show_about(self):
        """Displays a help message box."""
        QMessageBox.information(self, "About BMI Calculator",
                                "Enter your weight (kg) and height (cm), then click 'Calculate BMI' to see your result.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BMICalculator()
    window.show()
    sys.exit(app.exec())
