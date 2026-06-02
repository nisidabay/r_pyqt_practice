#!/usr/bin/env python3
"""Use self.sender() to identify which widget triggered the slot."""

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("sender() Demo")
        self.resize(300, 250)

        self.label = QLabel("Click a button")

        self.btn_a = QPushButton("Button A")
        self.btn_b = QPushButton("Button B")
        self.btn_c = QPushButton("Button C")

        self.btn_a.clicked.connect(self.on_any_button)
        self.btn_b.clicked.connect(self.on_any_button)
        self.btn_c.clicked.connect(self.on_any_button)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn_a)
        layout.addWidget(self.btn_b)
        layout.addWidget(self.btn_c)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def on_any_button(self):
        sender = self.sender()
        self.label.setText(f"Clicked: {sender.text()}")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
