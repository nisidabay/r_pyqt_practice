#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QStackedLayout, QPushButton,
                              QLabel, QVBoxLayout, QWidget, QHBoxLayout)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QStackedLayout")
        self.resize(300, 200)
        self.stack = QStackedLayout()
        self.stack.addWidget(self._page("Page 1", "lightgreen"))
        self.stack.addWidget(self._page("Page 2", "lightblue"))
        self.stack.addWidget(self._page("Page 3", "lightcoral"))
        btn_layout = QHBoxLayout()
        prev = QPushButton("← Prev")
        nxt = QPushButton("Next →")
        prev.clicked.connect(lambda: self._nav(-1))
        nxt.clicked.connect(lambda: self._nav(1))
        btn_layout.addWidget(prev)
        btn_layout.addWidget(nxt)
        main_layout = QVBoxLayout()
        main_layout.addLayout(self.stack)
        main_layout.addLayout(btn_layout)
        c = QWidget()
        c.setLayout(main_layout)
        self.setCentralWidget(c)

    def _page(self, text, color):
        label = QLabel(text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet(f"background-color: {color}; font-size: 24px;")
        return label

    def _nav(self, delta):
        idx = (self.stack.currentIndex() + delta) % self.stack.count()
        self.stack.setCurrentIndex(idx)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
