#!/usr/bin/env python3
"""Exercises: PyQt6 dialogs practice. Run me: python3 exercises.py"""
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QTimer

app = QApplication(sys.argv)

# === Ex 1: Confirmation message ===
class Ex1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ex1"); self.resize(250, 100)
        self.result = QLabel("Click button")
        btn = QPushButton("Delete?"); btn.clicked.connect(self._ask)
        layout = QVBoxLayout(); layout.addWidget(self.result); layout.addWidget(btn)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)
    def _ask(self):
        r = QMessageBox.question(self, "Delete", "Delete item?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        self.result.setText("Yes" if r == QMessageBox.StandardButton.Yes else "No")

w1 = Ex1(); w1.show()
print("Ex1: Confirmation dialog — auto close 2s")
QTimer.singleShot(2000, w1.close)
while w1.isVisible(): app.processEvents()
print(f"  Result: {w1.result.text()}"); print("-" * 40)

# === Ex 2: Input dialog ===
class Ex2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ex2"); self.resize(250, 100)
        self.result = QLabel("No input yet")
        btn = QPushButton("Get Name"); btn.clicked.connect(self._get)
        layout = QVBoxLayout(); layout.addWidget(self.result); layout.addWidget(btn)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)
    def _get(self):
        t, ok = QInputDialog.getText(self, "Name", "Your name:", text="Carlos")
        if ok: self.result.setText(f"Hello, {t}!")

w2 = Ex2(); w2.show()
print("Ex2: Input dialog — auto close 3s")
QTimer.singleShot(3000, w2.close)
while w2.isVisible(): app.processEvents()
print(f"  Result: {w2.result.text()}"); print("-" * 40)

# === Ex 3: Color picker ===
class Ex3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ex3"); self.resize(250, 120)
        self.label = QLabel("Color preview"); self.label.setAutoFillBackground(True)
        btn = QPushButton("Pick Color"); btn.clicked.connect(self._pick)
        layout = QVBoxLayout(); layout.addWidget(self.label); layout.addWidget(btn)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)
    def _pick(self):
        color = QColorDialog.getColor()
        if color.isValid():
            p = self.label.palette(); p.setColor(self.label.backgroundRole(), color)
            self.label.setPalette(p); self.label.setText(f"#{color.name()}")

w3 = Ex3(); w3.show()
print("Ex3: Color picker — auto close 3s")
QTimer.singleShot(3000, w3.close)
while w3.isVisible(): app.processEvents()
print(f"  Color: {w3.label.text()}"); print("-" * 40)

# === BONUS: Mini notepad ===
class Bonus(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini Notepad"); self.resize(400, 300)
        self.editor = QTextEdit()
        self.editor.setPlaceholderText("Type here...")
        open_btn = QPushButton("Open")
        save_btn = QPushButton("Save")
        font_btn = QPushButton("Font")
        open_btn.clicked.connect(self._open)
        save_btn.clicked.connect(self._save)
        font_btn.clicked.connect(self._font)
        btn_row = QHBoxLayout()
        btn_row.addWidget(open_btn); btn_row.addWidget(save_btn); btn_row.addWidget(font_btn)
        layout = QVBoxLayout(); layout.addWidget(self.editor); layout.addLayout(btn_row)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)
    def _open(self):
        p, _ = QFileDialog.getOpenFileName(self, "Open", "", "Text (*.txt);;All (*)")
        if p:
            with open(p) as f: self.editor.setText(f.read())
    def _save(self):
        p, _ = QFileDialog.getSaveFileName(self, "Save", "note.txt", "Text (*.txt)")
        if p:
            with open(p, "w") as f: f.write(self.editor.toPlainText())
    def _font(self):
        font, ok = QFontDialog.getFont(self.editor.font(), self)
        if ok: self.editor.setFont(font)

w4 = Bonus(); w4.show()
print("Bonus: Mini notepad — Open/Save/Font dialogs")
QTimer.singleShot(4000, w4.close)
while w4.isVisible(): app.processEvents()
print(f"  Editor text length: {len(w4.editor.toPlainText())}")
print("\nDone!")
sys.exit()
