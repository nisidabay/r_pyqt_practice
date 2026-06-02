#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QVBoxLayout, QWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox")
        self.resize(300, 200)
        self.label = QLabel("Select an option")
        combo = QComboBox()
        combo.addItems(["Python", "JavaScript", "Go", "Rust", "C++"])
        combo.setEditable(True)
        combo.setPlaceholderText("Type or select...")
        combo.currentTextChanged.connect(
            lambda t: self.label.setText(f"Selected: {t}" if t else "Select an option"))
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(combo)
        layout.addStretch()
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
