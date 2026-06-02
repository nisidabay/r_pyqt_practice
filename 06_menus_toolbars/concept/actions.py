#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTextEdit, QToolBar, QMessageBox)
from PyQt6.QtGui import QAction, QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shared Actions"); self.resize(400, 300)
        self.editor = QTextEdit(); self.setCentralWidget(self.editor)

        new_act = QAction("&New", self); new_act.setShortcut("Ctrl+N")
        new_act.triggered.connect(self.editor.clear)

        about_act = QAction("&About", self)
        about_act.triggered.connect(lambda: QMessageBox.about(self, "About", "v1.0"))

        file_menu = self.menuBar().addMenu("&File")
        file_menu.addAction(new_act)
        file_menu.addAction(about_act)

        tb = self.addToolBar("Main"); tb.addAction(new_act); tb.addAction(about_act)

app = QApplication(sys.argv); window = MainWindow(); window.show(); sys.exit(app.exec())
