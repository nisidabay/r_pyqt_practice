#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QInputDialog, QPushButton,
                              QVBoxLayout, QWidget, QLabel)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QInputDialog"); self.resize(300, 200)
        self.label = QLabel("Results appear here")
        layout = QVBoxLayout(); layout.addWidget(self.label)
        for text, slot in [("Get Text", self._text), ("Get Int", self._int),
                           ("Get Item", self._item)]:
            btn = QPushButton(text); btn.clicked.connect(slot); layout.addWidget(btn)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)

    def _text(self):
        t, ok = QInputDialog.getText(self, "Name", "Enter your name:")
        if ok: self.label.setText(f"Name: {t}")

    def _int(self):
        n, ok = QInputDialog.getInt(self, "Age", "Enter age:", 30, 1, 120)
        if ok: self.label.setText(f"Age: {n}")

    def _item(self):
        i, ok = QInputDialog.getItem(self, "Language", "Pick:", ["Python","Go","Rust"], 0, False)
        if ok: self.label.setText(f"Language: {i}")

app = QApplication(sys.argv); window = MainWindow(); window.show(); sys.exit(app.exec())
