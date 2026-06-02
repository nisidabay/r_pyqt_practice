#!/usr/bin/env python3
"""Color Tool — Pick a color, see hex/RGB values, copy hex to clipboard."""
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Color Tool")
        self.setFixedSize(350, 280)

        self.preview = QLabel("Pick a color")
        self.preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.preview.setAutoFillBackground(True)
        self.preview.setMinimumHeight(80)
        p = self.preview.palette()
        p.setColor(QPalette.ColorRole.Window, QColor("#cccccc"))
        self.preview.setPalette(p)

        self.hex_label = QLabel("HEX: #CCCCCC")
        self.rgb_label = QLabel("RGB: (204, 204, 204)")

        pick_btn = QPushButton("Pick Color")
        pick_btn.clicked.connect(self._pick)

        copy_btn = QPushButton("Copy HEX")
        copy_btn.clicked.connect(self._copy)

        layout = QVBoxLayout()
        layout.addWidget(self.preview)
        layout.addWidget(self.hex_label)
        layout.addWidget(self.rgb_label)
        layout.addWidget(pick_btn)
        layout.addWidget(copy_btn)

        c = QWidget()
        c.setLayout(layout)
        self.setCentralWidget(c)

    def _update(self, color):
        p = self.preview.palette()
        p.setColor(QPalette.ColorRole.Window, color)
        self.preview.setPalette(p)
        self.preview.setText(color.name().upper())
        self.hex_label.setText(f"HEX: {color.name().upper()}")
        self.rgb_label.setText(f"RGB: ({color.red()}, {color.green()}, {color.blue()})")

    def _pick(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self._update(color)

    def _copy(self):
        text = self.preview.text()
        QApplication.clipboard().setText(text)
        self.hex_label.setText(f"HEX: {text} ✓ (copied)")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
