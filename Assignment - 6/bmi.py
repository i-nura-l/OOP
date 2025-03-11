import os
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QHBoxLayout, QGridLayout, QFrame, QMenuBar, QMainWindow, QMessageBox)
from PyQt6.QtGui import QAction, QFont
from PyQt6 import uic

class Bmi(QMainWindow):
   def __init__(self):
       super(Bmi, self).__init__()

       self.input1 = QLineEdit( self)
       self.input2 = QLineEdit(self)
       self.result = QLabel(self)
       self.button1 = QPushButton(self)
       self.actionClear = QAction("Clear", self)
       self.actionExit = QAction("Exit", self)
       self.actionAbout = QAction("About", self)

       # MUST BE AFTER THE SELF THINGS FROM ABOVE
       ui_path = os.path.join(os.path.dirname(__file__), 'bmi.ui')
       uic.loadUi(ui_path, self)

       self.button1.clicked.connect(self.calculate)

       self.actionClear.triggered.connect(self.clear_fields)
       self.actionAbout.triggered.connect(self.show_about)
       self.actionExit.triggered.connect(self.close)

   def calculate(self):
       try:
           weight = float(self.input1.text())
           height = float(self.input2.text()) / 100

           bmi = round(weight / (height ** 2), 2)

           return self.result.setText(str(bmi))

       except ValueError:
           self.result.setText("Invalid input!")

   def clear_fields(self):
       """Clears the input fields."""
       self.input1.clear()
       self.input2.clear()
       self.result.setText("---")
       self.result.setStyleSheet("background-color: lightgray; padding: 10px; border-radius: 5px;")

   def show_about(self):
       """Displays a help message box."""
       QMessageBox.information(self, "About BMI Calculator",
                               "Enter your weight (kg) and height (cm), then click 'Calculate BMI' to see your result.")
