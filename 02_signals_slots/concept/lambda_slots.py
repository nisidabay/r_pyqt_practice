#!/usr/bin/env python3
"""Use lambda for quick inline slot functions."""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lambda Slots")
        self.resize(300, 200)

        self.label = QLabel("Counter: 0")
        self.count = 0

        inc_button = QPushButton("+1")
        reset_button = QPushButton("Reset")

        inc_button.clicked.connect(lambda: self._update_count(1))
        reset_button.clicked.connect(lambda: self._update_count(-self.count))

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(inc_button)
        layout.addWidget(reset_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def _update_count(self, delta):
        self.count += delta
        self.label.setText(f"Counter: {self.count}")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
