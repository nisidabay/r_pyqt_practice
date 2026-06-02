#!/usr/bin/env python3
"""Override closeEvent to ask the user before quitting."""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Close Confirmation")
        self.resize(300, 200)

        label = QLabel("Close this window to see the confirmation dialog")
        label.setWordWrap(True)
        self.setCentralWidget(label)

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            "Confirm Exit",
            "Are you sure you want to quit?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
