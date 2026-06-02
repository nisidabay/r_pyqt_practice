#!/usr/bin/env python3
"""Exercises: Layout practice — arrange widgets with PyQt6 layouts.

Run me: python3 exercises.py
"""
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QTimer

app = QApplication(sys.argv)

# === Ex 1: Vertical button stack ===
class Ex1VBox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VBox")
        self.resize(200, 220)
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("One"))
        layout.addWidget(QPushButton("Two"))
        layout.addWidget(QPushButton("Three"))
        layout.addStretch()
        layout.addWidget(QPushButton("Bottom"))
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)

w1 = Ex1VBox()
w1.show()
print("Ex1: Vertical stack — auto close 1s")
QTimer.singleShot(1000, w1.close)
while w1.isVisible(): app.processEvents()
print("-" * 40)

# === Ex 2: Grid of labels ===
class Ex2Grid(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid")
        self.resize(250, 200)
        layout = QGridLayout()
        colors = [("red", 0, 0), ("green", 0, 1), ("blue", 0, 2),
                  ("yellow", 1, 0), ("cyan", 1, 1), ("magenta", 1, 2)]
        for color, r, c in colors:
            label = QLabel(color)
            label.setStyleSheet(f"background-color: {color}; padding: 10px;")
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(label, r, c)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)

w2 = Ex2Grid()
w2.show()
print("Ex2: 2×3 color grid")
QTimer.singleShot(1500, w2.close)
while w2.isVisible(): app.processEvents()
print("-" * 40)

# === Ex 3: Login form ===
class Ex3Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.resize(300, 180)
        outer = QVBoxLayout()
        form = QFormLayout()
        form.addRow("Username:", QLineEdit())
        pw = QLineEdit()
        pw.setEchoMode(QLineEdit.EchoMode.Password)
        form.addRow("Password:", pw)
        outer.addLayout(form)
        btn_row = QHBoxLayout()
        btn_row.addStretch()
        btn_row.addWidget(QPushButton("Login"))
        outer.addLayout(btn_row)
        c = QWidget(); c.setLayout(outer); self.setCentralWidget(c)

w3 = Ex3Login()
w3.show()
print("Ex3: Login form — nested layouts")
QTimer.singleShot(1500, w3.close)
while w3.isVisible(): app.processEvents()
print("-" * 40)

# === BONUS: Stacked settings ===
class BonusStacked(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.resize(350, 220)
        self.stack = QStackedLayout()
        p1 = QWidget()
        l1 = QFormLayout(p1)
        l1.addRow("Username:", QLineEdit("carlos"))
        l1.addRow("Email:", QLineEdit("carlos@example.com"))
        p2 = QWidget()
        l2 = QVBoxLayout(p2)
        l2.addWidget(QCheckBox("Dark mode"))
        l2.addWidget(QCheckBox("Notifications"))
        l2.addStretch()
        self.stack.addWidget(p1)
        self.stack.addWidget(p2)
        nav = QHBoxLayout()
        prev = QPushButton("← General"); nxt = QPushButton("Advanced →")
        prev.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        nxt.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        nav.addWidget(prev); nav.addWidget(nxt)
        main = QVBoxLayout()
        main.addLayout(self.stack)
        main.addLayout(nav)
        c = QWidget(); c.setLayout(main); self.setCentralWidget(c)

w4 = BonusStacked()
w4.show()
print("Bonus: Stacked settings — General / Advanced pages")
QTimer.singleShot(3000, w4.close)
while w4.isVisible(): app.processEvents()
print("\nDone!")
sys.exit()
