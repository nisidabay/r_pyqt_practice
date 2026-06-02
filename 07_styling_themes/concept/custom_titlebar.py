#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton,
                              QVBoxLayout, QHBoxLayout, QWidget)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Title Bar")
        self.resize(400, 250)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        # Custom title bar
        title_bar = QWidget()
        title_bar.setFixedHeight(35)
        title_bar.setStyleSheet("background-color: #2b2b2b;")
        title_layout = QHBoxLayout(title_bar)
        title_layout.setContentsMargins(10, 0, 5, 0)
        title_layout.addWidget(QLabel("My Custom Window"))
        title_layout.addStretch()
        min_btn = QPushButton("_"); min_btn.setFixedSize(25, 25)
        min_btn.clicked.connect(self.showMinimized)
        close_btn = QPushButton("×"); close_btn.setFixedSize(25, 25)
        close_btn.clicked.connect(self.close)
        close_btn.setStyleSheet("QPushButton:hover { background-color: #d32f2f; }")
        title_layout.addWidget(min_btn); title_layout.addWidget(close_btn)
        # Content
        content = QLabel("Frameless window with custom title bar")
        content.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout = QVBoxLayout()
        main_layout.addWidget(title_bar)
        main_layout.addWidget(content)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        c = QWidget(); c.setLayout(main_layout); self.setCentralWidget(c)

app = QApplication(sys.argv)
window = MainWindow(); window.show(); sys.exit(app.exec())
