#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Selectors"); self.resize(300, 200)
        self.setStyleSheet("""
            QMainWindow { background-color: #1e1e1e; }
            QPushButton { background-color: #333; color: #ccc; padding: 8px; border: 1px solid #555; }
            QPushButton:hover { background-color: #444; color: white; }
            QPushButton#primary { background-color: #0078D7; color: white; font-weight: bold; }
            QPushButton#danger { background-color: #d32f2f; color: white; }
            QPushButton#danger:hover { background-color: #f44336; }""")
        layout = QVBoxLayout()
        for text in ["Normal Button", "Normal Button 2"]:
            layout.addWidget(QPushButton(text))
        p = QPushButton("Primary Action"); p.setObjectName("primary"); layout.addWidget(p)
        d = QPushButton("Delete"); d.setObjectName("danger"); layout.addWidget(d)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)

app = QApplication(sys.argv)
window = MainWindow(); window.show(); sys.exit(app.exec())
