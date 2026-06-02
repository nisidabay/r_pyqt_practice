#!/usr/bin/env python3
"""Multiple workers processing tasks from a queue — signals carry custom data."""
import sys, time, random
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QThread, pyqtSignal

class TaskWorker(QThread):
    task_done = pyqtSignal(str, int)  # (worker_name, result)

    def __init__(self, name, tasks):
        super().__init__()
        self._name = name; self._tasks = tasks

    def run(self):
        for task in self._tasks:
            time.sleep(random.uniform(0.5, 1.5))
            result = task * random.randint(2, 10)
            self.task_done.emit(self._name, result)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Worker Queue"); self.resize(400, 300)
        self.output = QTextEdit(); self.output.setReadOnly(True)
        btn = QPushButton("Start Workers"); btn.clicked.connect(self._start)
        layout = QVBoxLayout(); layout.addWidget(self.output); layout.addWidget(btn)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)

    def _start(self):
        self.output.clear()
        tasks = [1, 2, 3, 4, 5]
        for name in ["Worker A", "Worker B"]:
            w = TaskWorker(name, tasks)
            w.task_done.connect(lambda n, r: self.output.append(f"{n}: result={r}"))
            w.start()

app = QApplication(sys.argv); w = MainWindow(); w.show(); sys.exit(app.exec())
