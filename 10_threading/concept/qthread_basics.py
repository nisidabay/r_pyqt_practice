#!/usr/bin/env python3
"""QThread basics — run slow work in a background thread. UI stays responsive."""
import sys, time
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QThread, pyqtSignal

class Worker(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal(str)

    def run(self):
        for i in range(1, 6):
            time.sleep(1)
            self.progress.emit(i * 20)
        self.finished.emit("Done!")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QThread Basics"); self.resize(350, 250)
        self.label = QLabel("Ready")
        self.bar = QProgressBar()
        self.start_btn = QPushButton("Start"); self.start_btn.clicked.connect(self._start)
        self.cancel_btn = QPushButton("Cancel")
        layout = QVBoxLayout()
        layout.addWidget(self.label); layout.addWidget(self.bar)
        layout.addWidget(self.start_btn); layout.addWidget(self.cancel_btn)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)

    def _start(self):
        self.worker = Worker()
        self.worker.progress.connect(self.bar.setValue)
        self.worker.finished.connect(lambda msg: self.label.setText(msg))
        self.cancel_btn.clicked.connect(self.worker.terminate)
        self.worker.start()
        self.label.setText("Working...")

app = QApplication(sys.argv); w = MainWindow(); w.show(); sys.exit(app.exec())
