#!/usr/bin/env python3
"""Exercises: Create and configure PyQt6 windows.

Run me: python3 exercises.py
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt, QTimer


class Ex1Window(QMainWindow):
    """Exercise 1: Basic window — title and size."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First App")
        self.resize(400, 200)


class Ex2Window(QMainWindow):
    """Exercise 2: Center a 300×200 window on the primary screen."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Centered")
        self.resize(300, 200)
        self.center()

    def center(self):
        screen = self.screen().availableGeometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)


class Ex3Window(QMainWindow):
    """Exercise 3: Window with a centered label."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Label Window")
        self.resize(400, 150)

        label = QLabel("Hello, PyQt6!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)


class BonusWindow(QMainWindow):
    """Bonus: Auto-close after 2 seconds, print Goodbye! on close."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Auto-Close Bonus")
        self.resize(300, 100)

        label = QLabel("Closing in 2 seconds...")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)

        self.destroyed.connect(lambda: print("Goodbye!"))

        QTimer.singleShot(2000, self.close)


def run_exercise(window_class, label, delay_ms=1000):
    """Show a window for delay_ms then close it."""
    w = window_class()
    w.show()
    print(f"{label} — position: ({w.pos().x()}, {w.pos().y()}), size: ({w.width()}, {w.height()})")
    QTimer.singleShot(delay_ms, w.close)
    # Block until the window closes
    while w.isVisible():
        app.processEvents()
    print("-" * 40)


app = QApplication(sys.argv)

run_exercise(Ex1Window, "Exercise 1: Basic window")
run_exercise(Ex2Window, "Exercise 2: Centered window")
run_exercise(Ex3Window, "Exercise 3: Window with label")
print("Bonus: Watch for 'Goodbye!'...")
run_exercise(BonusWindow, "Bonus: Auto-close", delay_ms=2500)

print("\nAll exercises complete!")
sys.exit()
