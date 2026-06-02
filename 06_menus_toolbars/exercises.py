#!/usr/bin/env python3
"""Exercises: Menus and toolbars practice. Run me: python3 exercises.py"""
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt, QTimer

app = QApplication(sys.argv)

# === Ex 1: Simple menu ===
class Ex1(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle("Simple Menu"); self.resize(300, 200)
        self.editor = QTextEdit(); self.setCentralWidget(self.editor)
        fm = self.menuBar().addMenu("&File")
        for text, slot in [("&Clear", self.editor.clear), ("&Hello", lambda: self.editor.setText("Hello!"))]:
            a = QAction(text, self); a.triggered.connect(slot); fm.addAction(a)

w1 = Ex1(); w1.show()
print("Ex1: Simple menu — File → Clear, File → Hello")
QTimer.singleShot(2000, w1.close)
while w1.isVisible(): app.processEvents()
print(f"  Text: '{w1.editor.toPlainText()[:30]}'"); print("-" * 40)

# === Ex 2: Context menu ===
class Ex2(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle("Context Menu"); self.resize(300, 200)
        self.label = QLabel("Right-click me")
        self.label.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.label.customContextMenuRequested.connect(self._menu)
        self.setCentralWidget(self.label)
    def _menu(self, pos):
        menu = QMenu(self)
        menu.addAction("Green", lambda: self.label.setStyleSheet("color: green"))
        menu.addAction("Red", lambda: self.label.setStyleSheet("color: red"))
        menu.addAction("Reset", lambda: self.label.setStyleSheet(""))
        menu.exec(self.label.mapToGlobal(pos))

w2 = Ex2(); w2.show()
print("Ex2: Right-click context menu (Green/Red/Reset)")
QTimer.singleShot(2500, w2.close)
while w2.isVisible(): app.processEvents()
print("-" * 40)

# === Ex 3: Toolbar + shared action ===
class Ex3(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle("Toolbar + Menu"); self.resize(350, 250)
        self.label = QLabel("Use menu or toolbar"); self.setCentralWidget(self.label)
        clear_act = QAction("&Clear", self); clear_act.triggered.connect(lambda: self.label.setText("Cleared!"))
        hello_act = QAction("&Hello", self); hello_act.triggered.connect(lambda: self.label.setText("Hello!"))
        fm = self.menuBar().addMenu("&Actions")
        fm.addAction(clear_act); fm.addAction(hello_act)
        tb = self.addToolBar("Main"); tb.addAction(clear_act); tb.addAction(hello_act)

w3 = Ex3(); w3.show()
print("Ex3: Shared actions — menu & toolbar both work")
QTimer.singleShot(2500, w3.close)
while w3.isVisible(): app.processEvents()
print(f"  Label: '{w3.label.text()}'"); print("-" * 40)

# === BONUS: Text editor shell ===
class Bonus(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle("Editor Shell"); self.resize(450, 350)
        self.editor = QTextEdit(); self.setCentralWidget(self.editor)
        fm = self.menuBar().addMenu("&File")
        new = QAction("&New", self); new.setShortcut("Ctrl+N"); new.triggered.connect(self.editor.clear)
        fm.addAction(new); fm.addSeparator()
        ex = QAction("E&xit", self); ex.setShortcut("Ctrl+Q"); ex.triggered.connect(self.close)
        fm.addAction(ex)
        em = self.menuBar().addMenu("&Edit")
        em.addAction("Undo", self.editor.undo, "Ctrl+Z")
        em.addAction("Redo", self.editor.redo, "Ctrl+Y")
        em.addSeparator()
        em.addAction("Cut", self.editor.cut, "Ctrl+X")
        em.addAction("Copy", self.editor.copy, "Ctrl+C")
        em.addAction("Paste", self.editor.paste, "Ctrl+V")
        tb = self.addToolBar("Main")
        tb.addAction("Clear", self.editor.clear)
        sb = QStatusBar()
        self.char_label = QLabel("Chars: 0")
        self.editor.textChanged.connect(lambda: self.char_label.setText(
            f"Chars: {len(self.editor.toPlainText())}"))
        sb.addPermanentWidget(self.char_label); self.setStatusBar(sb)

w4 = Bonus(); w4.show()
w4.editor.setText("Hello from PyQt6!")
print("Bonus: Text editor with menus, toolbar, status bar")
QTimer.singleShot(3000, w4.close)
while w4.isVisible(): app.processEvents()
print(f"  Chars: {len(w4.editor.toPlainText())}"); print("\nDone!")
sys.exit()
