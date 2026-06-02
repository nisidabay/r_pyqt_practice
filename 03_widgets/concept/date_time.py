#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QDateEdit, QDateTimeEdit, QCalendarWidget, QVBoxLayout, QWidget, QLabel
from PyQt6.QtCore import QDate, QDateTime, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Date & Time")
        self.resize(350, 400)
        self.label = QLabel("Pick a date")
        date = QDateEdit(QDate.currentDate())
        date.setCalendarPopup(True)
        date.dateChanged.connect(lambda d: self.label.setText(f"Date: {d.toString('yyyy-MM-dd')}"))
        dt = QDateTimeEdit(QDateTime.currentDateTime())
        dt.dateTimeChanged.connect(lambda v: self.label.setText(f"DateTime: {v.toString('yyyy-MM-dd hh:mm:ss')}"))
        cal = QCalendarWidget()
        cal.clicked.connect(lambda d: self.label.setText(f"Calendar: {d.toString('yyyy-MM-dd')}"))
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(QLabel("Date:"))
        layout.addWidget(date)
        layout.addWidget(QLabel("DateTime:"))
        layout.addWidget(dt)
        layout.addWidget(QLabel("Calendar:"))
        layout.addWidget(cal)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
