#!/usr/bin/env python3
"""Thread reports incremental progress → QProgressBar stays responsive."""
import sys, time
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QThread, pyqtSignal

class Worker(QThread):
    progress = pyqtSignal(int)
    step_text = pyqtSignal(str)

    def run(self):
        tasks = ["Loading data...", "Processing...", "Validating...", "Saving...", "Done!"]
        for i, task in enumerate(tasks):
            time.sleep(1)
            self.progress.emit(i * 25)
            self.step_text.emit(task)
        self.progress.emit(100)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Thread Progress"); self.resize(400, 200)
        self.label = QLabel("Ready"); self.bar = QProgressBar()
        btn = QPushButton("Start"); btn.clicked.connect(self._start)
        layout = QVBoxLayout(); layout.addWidget(self.label)
        layout.addWidget(self.bar); layout.addWidget(btn)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)

    def _start(self):
        self.worker = Worker()
        self.worker.progress.connect(self.bar.setValue)
        self.worker.step_text.connect(self.label.setText)
        self.worker.start()

app = QApplication(sys.argv); w = MainWindow(); w.show(); sys.exit(app.exec())
