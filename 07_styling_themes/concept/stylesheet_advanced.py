#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTextEdit, QSlider, QVBoxLayout, QWidget)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Customized Scrollbar"); self.resize(400, 300)
        editor = QTextEdit()
        editor.setPlainText("\n".join([f"Line {i}" for i in range(50)]))
        self.setStyleSheet("""
            QMainWindow { background-color: #2b2b2b; }
            QTextEdit { background-color: #1e1e1e; color: #ccc; border: 1px solid #555; }
            QScrollBar:vertical { background: #2b2b2b; width: 12px; margin: 0; }
            QScrollBar::handle:vertical { background: #555; min-height: 20px; border-radius: 6px; }
            QScrollBar::handle:vertical:hover { background: #777; }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; }""")
        self.setCentralWidget(editor)

app = QApplication(sys.argv)
window = MainWindow(); window.show(); sys.exit(app.exec())
