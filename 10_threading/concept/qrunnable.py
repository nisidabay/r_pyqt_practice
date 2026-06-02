#!/usr/bin/env python3
"""QThreadPool + QRunnable — lightweight one-shot tasks, no thread management."""
import sys, time, random
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QRunnable, QThreadPool, pyqtSignal, QObject

class TaskSignals(QObject):
    done = pyqtSignal(int)

class Task(QRunnable):
    def __init__(self, task_id):
        super().__init__()
        self.id = task_id
        self.signals = TaskSignals()

    def run(self):
        time.sleep(random.uniform(0.5, 2))
        self.signals.done.emit(self.id)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QRunnable"); self.resize(350, 250)
        self.output = QTextEdit(); self.output.setReadOnly(True)
        self.pool = QThreadPool.globalInstance()
        self.pool.setMaxThreadCount(4)
        btn = QPushButton("Run 10 Tasks"); btn.clicked.connect(self._run)
        layout = QVBoxLayout(); layout.addWidget(self.output); layout.addWidget(btn)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)

    def _run(self):
        self.output.clear()
        for i in range(10):
            task = Task(i + 1)
            task.signals.done.connect(lambda tid: self.output.append(f"Task {tid} done"))
            self.pool.start(task)

app = QApplication(sys.argv); w = MainWindow(); w.show(); sys.exit(app.exec())
