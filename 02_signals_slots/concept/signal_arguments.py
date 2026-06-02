#!/usr/bin/env python3
"""Signals that carry data: textChanged, valueChanged, currentIndexChanged."""

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QSlider, QVBoxLayout, QWidget
)
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signal Arguments")
        self.resize(350, 250)

        # Text input → echo to label
        self.echo_label = QLabel("Type something...")
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Type here")
        self.text_input.textChanged.connect(self.on_text_changed)

        # Slider → number display
        self.slider_label = QLabel("Slider value: 50")
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.setValue(50)
        self.slider.valueChanged.connect(self.on_slider_changed)

        layout = QVBoxLayout()
        layout.addWidget(self.echo_label)
        layout.addWidget(self.text_input)
        layout.addSpacing(15)
        layout.addWidget(self.slider_label)
        layout.addWidget(self.slider)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def on_text_changed(self, text):
        self.echo_label.setText(f"You typed: {text}")

    def on_slider_changed(self, value):
        self.slider_label.setText(f"Slider value: {value}")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
