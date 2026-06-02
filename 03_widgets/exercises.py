#!/usr/bin/env python3
"""Exercises: Build forms with PyQt6 widgets.

Run me: python3 exercises.py
"""
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QTimer

app = QApplication(sys.argv)

# === Ex 1: Combo selector ===
class Ex1Combo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Combo Selector")
        self.resize(300, 120)
        self.label = QLabel("Pick a language")
        combo = QComboBox()
        combo.addItems(["Python", "Go", "Rust", "JavaScript"])
        combo.currentTextChanged.connect(lambda t: self.label.setText(f"Language: {t}"))
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(combo)
        c = QWidget()
        c.setLayout(layout)
        self.setCentralWidget(c)

w1 = Ex1Combo()
w1.show()
print("Ex1: Combo selector — auto close in 1s")
QTimer.singleShot(1000, w1.close)
while w1.isVisible(): app.processEvents()
print("-" * 40)

# === Ex 2: Toggle counter ===
class Ex2Toggle(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Toggle Counter")
        self.resize(250, 100)
        self.label = QLabel("Toggles: 0")
        self.count = 0
        chk = QCheckBox("Click to toggle")
        chk.toggled.connect(lambda v: self._inc(v))
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(chk)
        c = QWidget()
        c.setLayout(layout)
        self.setCentralWidget(c)
    def _inc(self, checked):
        self.count += 1
        self.label.setText(f"Toggles: {self.count} (checked={checked})")

w2 = Ex2Toggle()
w2.show()
print("Ex2: Toggle counter — click the checkbox")
QTimer.singleShot(2000, w2.close)
while w2.isVisible(): app.processEvents()
print(f"  Final toggles: {w2.count}")
print("-" * 40)

# === Ex 3: Password input ===
class Ex3Password(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Input")
        self.resize(300, 120)
        self.label = QLabel("Enter password")
        pw = QLineEdit()
        pw.setEchoMode(QLineEdit.EchoMode.Password)
        pw.setPlaceholderText("Password")
        pw.textChanged.connect(lambda t: self.label.setText(
            f"Length: {len(t)} chars" if t else "Enter password"))
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(pw)
        c = QWidget()
        c.setLayout(layout)
        self.setCentralWidget(c)

w3 = Ex3Password()
w3.show()
print("Ex3: Password field — type something")
QTimer.singleShot(2000, w3.close)
while w3.isVisible(): app.processEvents()
print("-" * 40)

# === BONUS: Profile form ===
class BonusProfile(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Profile Form")
        self.resize(350, 250)
        self.name = QLineEdit()
        self.name.setPlaceholderText("Full name")
        self.age = QSpinBox()
        self.age.setRange(1, 120)
        self.country = QComboBox()
        self.country.addItems(["Spain", "Mexico", "Argentina", "USA", "Other"])
        self.sub = QCheckBox("Subscribe to newsletter")
        self.result = QLabel("(not submitted)")
        btn = QPushButton("Submit")
        btn.clicked.connect(self._submit)
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Name:"))
        layout.addWidget(self.name)
        layout.addWidget(QLabel("Age:"))
        layout.addWidget(self.age)
        layout.addWidget(QLabel("Country:"))
        layout.addWidget(self.country)
        layout.addWidget(self.sub)
        layout.addWidget(btn)
        layout.addWidget(self.result)
        c = QWidget()
        c.setLayout(layout)
        self.setCentralWidget(c)
    def _submit(self):
        self.result.setText(
            f"Name: {self.name.text()}, Age: {self.age.value()}, "
            f"Country: {self.country.currentText()}, Subscribe: {self.sub.isChecked()}")

w4 = BonusProfile()
w4.show()
w4.name.setText("Carlos")
w4.age.setValue(57)
w4.country.setCurrentText("Spain")
w4.sub.setChecked(True)
print("Bonus: Profile form filled — watch for submit")
QTimer.singleShot(3000, w4.close)
while w4.isVisible(): app.processEvents()
print(f"  Submitted: {w4.result.text()}")
print("\nDone!")
sys.exit()
