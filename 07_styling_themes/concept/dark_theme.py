#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton,
                              QLineEdit, QVBoxLayout, QWidget, QCheckBox)
from PyQt6.QtGui import QPalette, QColor

DARK = {QPalette.ColorRole.Window: QColor(25, 25, 25),
    QPalette.ColorRole.WindowText: QColor(220, 220, 220),
    QPalette.ColorRole.Base: QColor(18, 18, 18),
    QPalette.ColorRole.Text: QColor(220, 220, 220),
    QPalette.ColorRole.Button: QColor(40, 40, 40),
    QPalette.ColorRole.ButtonText: QColor(220, 220, 220),
    QPalette.ColorRole.Highlight: QColor(86, 156, 214),
    QPalette.ColorRole.HighlightedText: QColor(25, 25, 25)}

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dark Theme"); self.resize(350, 250)
        p = QPalette()
        for role, color in DARK.items(): p.setColor(role, color)
        app.setPalette(p)
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Complete Dark Theme"))
        layout.addWidget(QLineEdit("Type here..."))
        layout.addWidget(QPushButton("Click Me"))
        layout.addWidget(QCheckBox("Remember me"))
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)

app = QApplication(sys.argv); app.setStyle("Fusion")
window = MainWindow(); window.show(); sys.exit(app.exec())
