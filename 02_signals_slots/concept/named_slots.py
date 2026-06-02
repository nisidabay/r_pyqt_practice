#!/usr/bin/env python3
"""Named methods as slots — cleaner for complex logic."""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import pyqtSlot


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Named Slots")
        self.resize(300, 200)

        self.result_label = QLabel("Ready")

        self.add_btn = QPushButton("Add Numbers")
        self.mult_btn = QPushButton("Multiply Numbers")

        self.add_btn.clicked.connect(self.calculate_sum)
        self.mult_btn.clicked.connect(self.calculate_product)

        layout = QVBoxLayout()
        layout.addWidget(self.result_label)
        layout.addWidget(self.add_btn)
        layout.addWidget(self.mult_btn)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    @pyqtSlot()
    def calculate_sum(self):
        numbers = [3, 7, 12, 5]
        result = sum(numbers)
        self.result_label.setText(f"3 + 7 + 12 + 5 = {result}")

    @pyqtSlot()
    def calculate_product(self):
        numbers = [3, 7, 12, 5]
        result = 1
        for n in numbers:
            result *= n
        self.result_label.setText(f"3 × 7 × 12 × 5 = {result}")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
