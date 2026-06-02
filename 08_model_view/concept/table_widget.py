#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTableWidget"); self.resize(450, 300)
        self.table = QTableWidget(5, 3)
        self.table.setHorizontalHeaderLabels(["Name", "Role", "Active"])
        data = [("Alice", "Developer", "Yes"), ("Bob", "Designer", "No"),
                ("Carol", "Manager", "Yes"), ("Dave", "Tester", "Yes"), ("Eve", "PM", "No")]
        for r, (name, role, active) in enumerate(data):
            self.table.setItem(r, 0, QTableWidgetItem(name))
            self.table.setItem(r, 1, QTableWidgetItem(role))
            self.table.setItem(r, 2, QTableWidgetItem(active))
        self.table.resizeColumnsToContents()
        self.table.itemClicked.connect(lambda i: self.statusBar().showMessage(f"Clicked: {i.text()}"))
        self.setStatusBar(QStatusBar())
        self.setCentralWidget(self.table)

app = QApplication(sys.argv); w = MainWindow(); w.show(); sys.exit(app.exec())
