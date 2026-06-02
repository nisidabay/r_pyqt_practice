#!/usr/bin/env python3
"""Define your own signals with pyqtSignal for custom communication."""

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
)
from PyQt6.QtCore import pyqtSignal, QObject


class Counter(QObject):
    """A non-widget object that emits signals when the count changes."""
    value_changed = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self._count = 0

    def increment(self):
        self._count += 1
        self.value_changed.emit(self._count)

    def reset(self):
        self._count = 0
        self.value_changed.emit(self._count)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Signal")
        self.resize(300, 200)

        self.counter = Counter()
        self.counter.value_changed.connect(self.on_count_changed)

        self.label = QLabel("Count: 0")

        inc_btn = QPushButton("Increment")
        inc_btn.clicked.connect(self.counter.increment)

        reset_btn = QPushButton("Reset")
        reset_btn.clicked.connect(self.counter.reset)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(inc_btn)
        layout.addWidget(reset_btn)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def on_count_changed(self, value):
        self.label.setText(f"Count: {value}")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
