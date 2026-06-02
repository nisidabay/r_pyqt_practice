#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QFontDialog, QPushButton,
                              QLabel, QVBoxLayout, QWidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFontDialog"); self.resize(350, 200)
        self.label = QLabel("Sample text — click button to change font")
        btn = QPushButton("Choose Font"); btn.clicked.connect(self._pick)
        layout = QVBoxLayout(); layout.addWidget(self.label); layout.addWidget(btn)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)

    def _pick(self):
        font, ok = QFontDialog.getFont(self.label.font(), self)
        if ok: self.label.setFont(font)

app = QApplication(sys.argv); window = MainWindow(); window.show(); sys.exit(app.exec())
