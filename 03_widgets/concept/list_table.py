#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QListWidget, QTableWidget,
                              QTableWidgetItem, QVBoxLayout, QWidget, QLabel, QPushButton,
                              QHBoxLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lists & Tables")
        self.resize(400, 350)
        self.label = QLabel("Click an item")
        lw = QListWidget()
        lw.addItems(["Apple", "Banana", "Cherry", "Date", "Elderberry"])
        lw.currentTextChanged.connect(lambda t: self.label.setText(f"List: {t}"))
        tw = QTableWidget(3, 2)
        tw.setHorizontalHeaderLabels(["Name", "Score"])
        data = [("Alice", "95"), ("Bob", "87"), ("Carol", "92")]
        for row, (name, score) in enumerate(data):
            tw.setItem(row, 0, QTableWidgetItem(name))
            tw.setItem(row, 1, QTableWidgetItem(score))
        tw.itemClicked.connect(
            lambda item: self.label.setText(
                f"Table: row {item.row()}, col {item.column()}: {item.text()}"))
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(QLabel("QListWidget:"))
        layout.addWidget(lw)
        layout.addWidget(QLabel("QTableWidget:"))
        layout.addWidget(tw)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
