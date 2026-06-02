#!/usr/bin/env python3
"""Profile Form — Fill in personal info and submit to console."""
import sys, json
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Profile Form")
        self.resize(400, 350)
        form = QFormLayout()
        self.fields = {}
        self.fields["name"] = QLineEdit()
        self.fields["name"].setPlaceholderText("Your name")
        self.fields["email"] = QLineEdit()
        self.fields["email"].setPlaceholderText("email@example.com")
        self.fields["age"] = QSpinBox()
        self.fields["age"].setRange(1, 120)
        self.fields["age"].setValue(30)
        self.fields["country"] = QComboBox()
        self.fields["country"].addItems(["Spain", "Mexico", "Argentina", "Colombia", "USA", "Other"])
        self.fields["subscribe"] = QCheckBox("Subscribe to newsletter")
        form.addRow("Name:", self.fields["name"])
        form.addRow("Email:", self.fields["email"])
        form.addRow("Age:", self.fields["age"])
        form.addRow("Country:", self.fields["country"])
        form.addRow("", self.fields["subscribe"])
        self.result = QLabel("")
        self.result.setWordWrap(True)
        submit = QPushButton("Submit")
        submit.clicked.connect(self._submit)
        vlayout = QVBoxLayout()
        vlayout.addLayout(form)
        vlayout.addWidget(submit)
        vlayout.addWidget(self.result)
        c = QWidget()
        c.setLayout(vlayout)
        self.setCentralWidget(c)

    def _submit(self):
        data = {name: w.text() if hasattr(w, 'text') else
                w.value() if hasattr(w, 'value') else w.isChecked()
                for name, w in self.fields.items()}
        self.result.setText(f"Submitted!\n{json.dumps(data, indent=2)}")
        print(json.dumps(data, indent=2))

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
