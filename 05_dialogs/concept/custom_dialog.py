#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QDialog, QDialogButtonBox,
                              QFormLayout, QLineEdit, QPushButton, QVBoxLayout, QWidget, QLabel)

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Login"); self.setFixedSize(300, 150)
        layout = QFormLayout(self)
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addRow("Username:", self.username)
        layout.addRow("Password:", self.password)
        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        buttons.accepted.connect(self.accept); buttons.rejected.connect(self.reject)
        layout.addRow(buttons)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Dialog"); self.resize(300, 150)
        self.label = QLabel("Click to login")
        btn = QPushButton("Login..."); btn.clicked.connect(self._login)
        layout = QVBoxLayout(); layout.addWidget(self.label); layout.addWidget(btn)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)

    def _login(self):
        dlg = LoginDialog(self)
        if dlg.exec() == QDialog.DialogCode.Accepted:
            self.label.setText(f"Welcome, {dlg.username.text()}!")
        else:
            self.label.setText("Login cancelled")

app = QApplication(sys.argv); window = MainWindow(); window.show(); sys.exit(app.exec())
