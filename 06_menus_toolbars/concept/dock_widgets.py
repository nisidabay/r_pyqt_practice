#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTextEdit, QDockWidget, QListWidget)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dock Widgets"); self.resize(500, 350)
        self.setCentralWidget(QTextEdit())
        dock = QDockWidget("File Browser", self)
        dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea | Qt.DockWidgetArea.RightDockWidgetArea)
        files = QListWidget(); files.addItems(["document.txt", "notes.md", "script.py", "data.json"])
        dock.setWidget(files)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock)

app = QApplication(sys.argv); window = MainWindow(); window.show(); sys.exit(app.exec())
