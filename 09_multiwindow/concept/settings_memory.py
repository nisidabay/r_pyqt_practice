#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QSettings

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSettings"); self.resize(400, 300)
        self.settings = QSettings("MyApp", "Demo")
        geo = self.settings.value("geometry")
        if geo: self.restoreGeometry(geo)
        self.label = QLabel("Resize and move this window.\nClose it — geometry is saved.")
        self.label.setAlignment(type(self.label.alignment()).AlignCenter)
        self.setCentralWidget(self.label)
    def closeEvent(self, event):
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

app = QApplication(sys.argv); app.setOrganizationName("MyApp"); app.setApplicationName("Demo")
w = MainWindow(); w.show(); sys.exit(app.exec())
