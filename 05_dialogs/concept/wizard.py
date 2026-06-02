#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWizard, QWizardPage, QLabel,
                              QLineEdit, QVBoxLayout, QPushButton, QWidget)

class Page1(QWizardPage):
    def __init__(self):
        super().__init__(); self.setTitle("Personal Info")
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Name:")); layout.addWidget(QLineEdit())

class Page2(QWizardPage):
    def __init__(self):
        super().__init__(); self.setTitle("Preferences")
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Theme:")); layout.addWidget(QLineEdit())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QWizard"); self.resize(300, 150)
        btn = QPushButton("Start Wizard"); btn.clicked.connect(self._wizard)
        c = QWidget(); c.setLayout(QVBoxLayout())
        c.layout().addWidget(btn); self.setCentralWidget(c)

    def _wizard(self):
        wiz = QWizard(self)
        wiz.addPage(Page1()); wiz.addPage(Page2())
        if wiz.exec() == QWizard.DialogCode.Accepted:
            print("Wizard finished")

app = QApplication(sys.argv); window = MainWindow(); window.show(); sys.exit(app.exec())
