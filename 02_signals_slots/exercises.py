#!/usr/bin/env python3
"""Exercises: Signals and slots — connect widgets to actions.

Run me: python3 exercises.py
"""

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QLineEdit,
    QSlider, QProgressBar, QVBoxLayout, QWidget
)
from PyQt6.QtCore import Qt, QTimer

# Use a single QApplication
app = QApplication(sys.argv)


# === Exercise 1: Button Counter ===
# Task: +/- buttons that update a counter label.

class Ex1Counter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Counter")
        self.resize(250, 150)

        self.count = 0
        self.label = QLabel("Count: 0")

        inc = QPushButton("+")
        dec = QPushButton("-")
        inc.clicked.connect(lambda: self._change(1))
        dec.clicked.connect(lambda: self._change(-1))

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(inc)
        layout.addWidget(dec)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def _change(self, delta):
        self.count += delta
        self.label.setText(f"Count: {self.count}")


w1 = Ex1Counter()
w1.show()
print("Exercise 1: Click +/- buttons (auto-closes in 3s)")
QTimer.singleShot(3000, w1.close)
while w1.isVisible():
    app.processEvents()
print(f"  Final count: {w1.count}")
print("-" * 40)


# === Exercise 2: Slider → Progress Bar ===
# Task: Sync a horizontal slider with a progress bar.

class Ex2Slider(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slider → Progress")
        self.resize(350, 120)

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 100)
        self.progress = QProgressBar()

        self.slider.valueChanged.connect(self.progress.setValue)

        layout = QVBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(self.progress)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


w2 = Ex2Slider()
w2.show()
w2.slider.setValue(75)
print("Exercise 2: Slider at 75, progress bar synced")
QTimer.singleShot(2000, w2.close)
while w2.isVisible():
    app.processEvents()
print(f"  Slider: {w2.slider.value()}, Progress: {w2.progress.value()}")
print("-" * 40)


# === Exercise 3: Text Echo ===
# Task: Type in a QLineEdit, echo to a label in real time.

class Ex3Echo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Echo")
        self.resize(350, 120)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Type something...")
        self.label = QLabel("(nothing yet)")

        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


w3 = Ex3Echo()
w3.show()
w3.input.setText("Hello PyQt6!")
print("Exercise 3: Typed 'Hello PyQt6!', label shows it")
QTimer.singleShot(1500, w3.close)
while w3.isVisible():
    app.processEvents()
print(f"  Label text: '{w3.label.text()}'")
print("-" * 40)


# === BONUS: Submit Form ===
# Task: Text input + Submit button. Click copies text to label, clears input.

class BonusForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Submit Form")
        self.resize(350, 150)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Enter your name...")
        self.label = QLabel("(not submitted yet)")
        submit = QPushButton("Submit")
        submit.clicked.connect(self._on_submit)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(submit)
        layout.addWidget(self.label)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def _on_submit(self):
        text = self.input.text()
        self.label.setText(f"Submitted: {text}")
        self.input.clear()


w4 = BonusForm()
w4.show()
print("Bonus: Type name and click Submit (auto-closes in 4s)")
QTimer.singleShot(4000, w4.close)
while w4.isVisible():
    app.processEvents()
print(f"  Label: '{w4.label.text()}'")
print(f"  Input cleared: '{w4.input.text()}'")

print("\nAll exercises complete!")
sys.exit()
