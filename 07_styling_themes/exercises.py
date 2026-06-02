#!/usr/bin/env python3
"""Exercises: Styling practice. Run me: python3 exercises.py"""
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt, QTimer

app = QApplication(sys.argv)

# === Ex 1: Hover button ===
class Ex1(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle("Hover"); self.resize(250, 150)
        btn = QPushButton("Hover over me")
        btn.setStyleSheet("QPushButton { background: #0078D7; color: white; padding: 20px; border-radius: 8px; } QPushButton:hover { background: #005a9e; }")
        self.setCentralWidget(btn)
w1 = Ex1(); w1.show()
print("Ex1: Hover-styled button")
QTimer.singleShot(1500, w1.close)
while w1.isVisible(): app.processEvents()
print("-" * 40)

# === Ex 2: Dark form ===
class Ex2(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle("Dark Form"); self.resize(300, 220)
        p = QPalette()
        p.setColor(QPalette.ColorRole.Window, QColor(40, 40, 40))
        p.setColor(QPalette.ColorRole.WindowText, QColor(220, 220, 220))
        p.setColor(QPalette.ColorRole.Base, QColor(30, 30, 30))
        p.setColor(QPalette.ColorRole.Text, QColor(220, 220, 220))
        p.setColor(QPalette.ColorRole.Button, QColor(55, 55, 55))
        p.setColor(QPalette.ColorRole.ButtonText, QColor(220, 220, 220))
        app.setStyle("Fusion"); app.setPalette(p)
        layout = QFormLayout()
        layout.addRow("Name:", QLineEdit())
        layout.addRow("Email:", QLineEdit())
        layout.addRow(QPushButton("Submit"))
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)
w2 = Ex2(); w2.show()
print("Ex2: Dark themed form")
QTimer.singleShot(2000, w2.close)
while w2.isVisible(): app.processEvents()
print("-" * 40)

# === Ex 3: Toggle theme ===
class Ex3(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle("Theme Toggle"); self.resize(300, 200)
        self.dark = True; self._apply_dark()
        self.label = QLabel("Dark mode active")
        self.btn = QPushButton("Toggle Theme"); self.btn.clicked.connect(self._toggle)
        layout = QVBoxLayout(); layout.addWidget(self.label); layout.addWidget(self.btn)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)
    def _apply_dark(self):
        p = QPalette()
        p.setColor(QPalette.ColorRole.Window, QColor(40, 40, 40))
        p.setColor(QPalette.ColorRole.WindowText, QColor(220, 220, 220))
        p.setColor(QPalette.ColorRole.Button, QColor(55, 55, 55))
        p.setColor(QPalette.ColorRole.ButtonText, QColor(220, 220, 220))
        app.setStyle("Fusion"); app.setPalette(p)
    def _apply_light(self): app.setStyle("Fusion"); app.setPalette(QApplication.style().standardPalette())
    def _toggle(self):
        self.dark = not self.dark
        if self.dark: self._apply_dark(); self.label.setText("Dark mode active")
        else: self._apply_light(); self.label.setText("Light mode active")
w3 = Ex3(); w3.show()
print("Ex3: Theme toggle — dark/light palette")
QTimer.singleShot(3000, w3.close)
while w3.isVisible(): app.processEvents()
print(f"  Mode: {w3.label.text()}"); print("-" * 40)

# === BONUS: Widget gallery ===
class Bonus(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle("Widget Gallery"); self.resize(400, 350)
        self.dark = True; self._apply_dark()
        self.setStyleSheet("""
            QPushButton#toggle { background: #0078D7; color: white; padding: 8px 16px; border-radius: 4px; }
            QPushButton#toggle:hover { background: #005a9e; }
            QGroupBox { color: #ccc; border: 1px solid #555; margin-top: 10px; padding-top: 10px; }
            QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 5px; }""")
        main = QVBoxLayout()
        self.toggle_btn = QPushButton("Switch to Light"); self.toggle_btn.setObjectName("toggle")
        self.toggle_btn.clicked.connect(self._toggle); main.addWidget(self.toggle_btn)
        gb = QGroupBox("Controls")
        gl = QVBoxLayout(gb); gl.addWidget(QCheckBox("Option 1")); gl.addWidget(QCheckBox("Option 2"))
        gl.addWidget(QPushButton("Action")); gl.addWidget(QSlider(Qt.Orientation.Horizontal))
        main.addWidget(gb)
        c = QWidget(); c.setLayout(main); self.setCentralWidget(c)
    def _apply_dark(self):
        p = QPalette()
        p.setColor(QPalette.ColorRole.Window, QColor(40, 40, 40))
        p.setColor(QPalette.ColorRole.WindowText, QColor(220, 220, 220))
        p.setColor(QPalette.ColorRole.Button, QColor(55, 55, 55))
        p.setColor(QPalette.ColorRole.ButtonText, QColor(220, 220, 220))
        app.setStyle("Fusion"); app.setPalette(p)
    def _toggle(self):
        self.dark = not self.dark
        if self.dark: self._apply_dark(); self.toggle_btn.setText("Switch to Light")
        else: app.setPalette(QApplication.style().standardPalette()); self.toggle_btn.setText("Switch to Dark")
w4 = Bonus(); w4.show()
print("Bonus: Theme switcher with widget gallery")
QTimer.singleShot(3500, w4.close)
while w4.isVisible(): app.processEvents()
print(f"  Dark mode: {w4.dark}"); print("\nDone!")
sys.exit()
