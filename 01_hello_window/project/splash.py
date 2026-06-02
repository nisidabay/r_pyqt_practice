#!/usr/bin/env python3
"""Splash screen — appears for 2 seconds then launches the main window."""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QSplashScreen
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap, QColor, QPainter


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Application")
        self.resize(500, 300)

        label = QLabel("Welcome! The splash screen has closed.")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)


def create_splash():
    # Create a small pixmap with app branding
    pixmap = QPixmap(400, 200)
    pixmap.fill(QColor(53, 53, 53))

    painter = QPainter(pixmap)
    painter.setPen(QColor(255, 255, 255))
    font = painter.font()
    font.setPointSize(24)
    painter.setFont(font)
    painter.drawText(pixmap.rect(), Qt.AlignmentFlag.AlignCenter, "MyApp v1.0")
    painter.end()

    splash = QSplashScreen(pixmap)
    splash.show()
    return splash


app = QApplication(sys.argv)

splash = create_splash()
splash.showMessage("Loading...", Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter, Qt.GlobalColor.white)

# Simulate loading, then show main window
def show_main():
    window = MainWindow()
    window.show()
    splash.finish(window)

QTimer.singleShot(2000, show_main)

sys.exit(app.exec())
