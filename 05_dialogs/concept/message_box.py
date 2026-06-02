#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QPushButton, QVBoxLayout, QWidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox")
        self.resize(300, 250)
        layout = QVBoxLayout()
        for text, slot in [("Info", self._info), ("Warning", self._warn),
                           ("Critical", self._critical), ("Question", self._question)]:
            btn = QPushButton(text); btn.clicked.connect(slot); layout.addWidget(btn)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)
    def _info(self): QMessageBox.information(self, "Info", "Operation completed.")
    def _warn(self): QMessageBox.warning(self, "Warning", "Disk space low.")
    def _critical(self): QMessageBox.critical(self, "Error", "Operation failed!")
    def _question(self):
        r = QMessageBox.question(self, "Confirm", "Delete this file?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        print("Yes" if r == QMessageBox.StandardButton.Yes else "No")

app = QApplication(sys.argv); window = MainWindow(); window.show(); sys.exit(app.exec())
