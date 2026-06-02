#!/usr/bin/env python3
"""Exercises: Threading practice. Run me: python3 exercises.py"""
import sys, time
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QThread, pyqtSignal, QTimer

app = QApplication(sys.argv)

# === Ex 1: Simple QThread ===
class SimpleWorker(QThread):
    done = pyqtSignal(int)
    def run(self):
        time.sleep(1); self.done.emit(42)

class Ex1(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle("Simple Thread"); self.resize(250, 120)
        self.label = QLabel("Result: —"); btn = QPushButton("Run")
        btn.clicked.connect(lambda: self._run())
        l = QVBoxLayout(); l.addWidget(self.label); l.addWidget(btn)
        c = QWidget(); c.setLayout(l); self.setCentralWidget(c)
    def _run(self):
        self.label.setText("Running..."); self.w = SimpleWorker()
        self.w.done.connect(lambda v: self.label.setText(f"Result: {v}")); self.w.start()

w1 = Ex1(); w1.show()
print("Ex1: Simple thread returns 42 after 1 second")
QTimer.singleShot(2500, w1.close)
while w1.isVisible(): app.processEvents()
print(f"  {w1.label.text()}"); print("-" * 40)

# === Ex 2: Progress bar ===
class ProgressWorker(QThread):
    progress = pyqtSignal(int)
    def run(self):
        for i in range(0, 101, 20): time.sleep(0.3); self.progress.emit(i)

class Ex2(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle("Progress"); self.resize(350, 120)
        self.bar = QProgressBar(); btn = QPushButton("Start")
        btn.clicked.connect(lambda: (btn.setEnabled(False), self._run()))
        l = QVBoxLayout(); l.addWidget(self.bar); l.addWidget(btn)
        c = QWidget(); c.setLayout(l); self.setCentralWidget(c)
    def _run(self):
        self.w = ProgressWorker()
        self.w.progress.connect(self.bar.setValue); self.w.start()

w2 = Ex2(); w2.show()
print("Ex2: Thread-driven progress bar")
QTimer.singleShot(3000, w2.close)
while w2.isVisible(): app.processEvents()
print(f"  Bar value: {w2.bar.value()}"); print("-" * 40)

# === Ex 3: Cancel worker ===
class CancelWorker(QThread):
    tick = pyqtSignal(int)
    def run(self):
        for i in range(100): time.sleep(0.05); self.tick.emit(i)

class Ex3(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle("Cancel"); self.resize(350, 150)
        self.label = QLabel("Ready"); self.bar = QProgressBar()
        start = QPushButton("Start"); cancel = QPushButton("Cancel")
        start.clicked.connect(self._start); cancel.clicked.connect(self._cancel)
        row = QHBoxLayout(); row.addWidget(start); row.addWidget(cancel)
        l = QVBoxLayout(); l.addWidget(self.label); l.addWidget(self.bar); l.addLayout(row)
        c = QWidget(); c.setLayout(l); self.setCentralWidget(c)
    def _start(self):
        self.w = CancelWorker()
        self.w.tick.connect(lambda v: (self.bar.setValue(v), self.label.setText(f"Tick: {v}")))
        self.w.start()
    def _cancel(self):
        if hasattr(self, 'w') and self.w.isRunning():
            self.w.terminate(); self.label.setText("Cancelled!")

w3 = Ex3(); w3.show()
print("Ex3: Start then Cancel — worker terminates mid-progress")
QTimer.singleShot(2500, w3.close)
while w3.isVisible(): app.processEvents()
print(f"  Final: {w3.label.text()}"); print("-" * 40)

# === BONUS: File counter ===
import os
class FileCounter(QThread):
    found = pyqtSignal(str)
    done = pyqtSignal(int)

    def __init__(self, directory):
        super().__init__(); self._dir = directory
    def run(self):
        count = 0
        for root, dirs, files in os.walk(self._dir):
            for f in files: count += 1; self.found.emit(os.path.join(root, f))
        self.done.emit(count)

class Bonus(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle("File Counter"); self.resize(450, 300)
        self.dir_input = QLineEdit(os.path.expanduser("~"))
        self.output = QTextEdit(); self.output.setReadOnly(True)
        self.count_label = QLabel("Files: 0")
        btn = QPushButton("Count"); btn.clicked.connect(self._count)
        l = QVBoxLayout(); l.addWidget(QLabel("Directory:")); l.addWidget(self.dir_input)
        l.addWidget(self.count_label); l.addWidget(self.output); l.addWidget(btn)
        c = QWidget(); c.setLayout(l); self.setCentralWidget(c)
    def _count(self):
        self.output.clear(); self.worker = FileCounter(self.dir_input.text())
        self.worker.found.connect(lambda f: self.output.append(f))
        self.worker.done.connect(lambda c: self.count_label.setText(f"Files: {c}"))
        self.worker.start()

w4 = Bonus(); w4.show()
print("Bonus: File counter — scan home dir in background thread")
QTimer.singleShot(5000, w4.close)
while w4.isVisible(): app.processEvents()
print(f"  {w4.count_label.text()}"); print("\nDone!"); sys.exit()
