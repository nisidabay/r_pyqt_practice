#!/usr/bin/env python3
"""Exercises: Multi-window practice. Run me: python3 exercises.py"""
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QTimer, pyqtSignal, QObject

app = QApplication(sys.argv)

# === Ex 1: Sub-window ===
class Sub(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent); self.setWindowTitle("Sub"); self.resize(250, 100)
        self.setCentralWidget(QLabel("I am a sub-window!"))

class Ex1(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle("Main"); self.resize(250, 100)
        open_btn = QPushButton("Open Sub"); open_btn.clicked.connect(lambda: Sub(self).show())
        self.setCentralWidget(open_btn)
w1 = Ex1(); w1.show()
print("Ex1: Sub-window — click to open")
QTimer.singleShot(2000, w1.close)
while w1.isVisible(): app.processEvents()
print("-" * 40)

# === Ex 2: Modal dialog ===
class Ex2(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle("Modal"); self.resize(250, 100)
        self.label = QLabel("Waiting...")
        btn = QPushButton("Open Modal"); btn.clicked.connect(self._modal)
        l = QVBoxLayout(); l.addWidget(self.label); l.addWidget(btn)
        c = QWidget(); c.setLayout(l); self.setCentralWidget(c)
    def _modal(self):
        dlg = QDialog(self); dlg.setModal(True); dlg.setWindowTitle("Modal"); dlg.resize(200, 100)
        dlg.setLayout(QVBoxLayout()); dlg.layout().addWidget(QLabel("Blocking..."))
        ok = QPushButton("OK"); ok.clicked.connect(dlg.accept); dlg.layout().addWidget(ok)
        dlg.exec(); self.label.setText("Dialog closed")
w2 = Ex2(); w2.show()
print("Ex2: Modal dialog — blocks main window")
QTimer.singleShot(2500, w2.close)
while w2.isVisible(): app.processEvents()
print(f"  Status: {w2.label.text()}"); print("-" * 40)

# === Ex 3: Signal between windows ===
class Notifier(QObject): message = pyqtSignal(str)

class Ex3(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle("Signal Across Windows"); self.resize(300, 150)
        self.notifier = Notifier()
        self.label = QLabel("No messages")
        btn = QPushButton("Open Sub")
        btn.clicked.connect(self._open); self.notifier.message.connect(lambda m: self.label.setText(f"Received: {m}"))
        l = QVBoxLayout(); l.addWidget(self.label); l.addWidget(btn)
        c = QWidget(); c.setLayout(l); self.setCentralWidget(c)
    def _open(self):
        sub = QMainWindow(self); sub.setWindowTitle("Sender"); sub.resize(200, 100)
        b = QPushButton("Send 'Hi!'")
        b.clicked.connect(lambda: self.notifier.message.emit("Hi!")); sub.setCentralWidget(b); sub.show()
w3 = Ex3(); w3.show()
print("Ex3: Signal between windows — open sub, click Send")
QTimer.singleShot(3000, w3.close)
while w3.isVisible(): app.processEvents()
print(f"  Message: {w3.label.text()}"); print("-" * 40)

# === BONUS: Settings window ===
class SettingsDialog(QDialog):
    settings_changed = pyqtSignal(str, str)
    def __init__(self, parent=None):
        super().__init__(parent); self.setWindowTitle("Settings"); self.setModal(True); self.resize(300, 200)
        l = QFormLayout(self)
        self.name = QLineEdit(); self.theme = QComboBox(); self.theme.addItems(["Light", "Dark"])
        l.addRow("Username:", self.name); l.addRow("Theme:", self.theme)
        bb = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        bb.accepted.connect(self._apply); bb.rejected.connect(self.reject); l.addRow(bb)
    def _apply(self):
        self.settings_changed.emit(self.name.text(), self.theme.currentText()); self.accept()

class Bonus(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle("Main App"); self.resize(350, 150)
        self.user_label = QLabel("Username: (none)"); self.theme_label = QLabel("Theme: (none)")
        btn = QPushButton("Settings..."); btn.clicked.connect(self._settings)
        l = QVBoxLayout(); l.addWidget(self.user_label); l.addWidget(self.theme_label); l.addWidget(btn)
        c = QWidget(); c.setLayout(l); self.setCentralWidget(c)
    def _settings(self):
        dlg = SettingsDialog(self)
        dlg.settings_changed.connect(lambda name, theme: (self.user_label.setText(f"Username: {name}"), self.theme_label.setText(f"Theme: {theme}")))
        dlg.exec()
w4 = Bonus(); w4.show()
print("Bonus: Settings window → updates main window via signal")
QTimer.singleShot(4000, w4.close)
while w4.isVisible(): app.processEvents()
print(f"  {w4.user_label.text()}, {w4.theme_label.text()}")
print("\nDone!"); sys.exit()
