#!/usr/bin/env python3
"""Button click → slot: the fundamental PyQt interaction pattern."""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signal Basics")
        self.resize(300, 150)

        self.label = QLabel("Click the button")
        self.button = QPushButton("Click Me")
        self.button.clicked.connect(self.on_button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def on_button_clicked(self):
        self.label.setText("Button was clicked!")
        self.button.setEnabled(False)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
