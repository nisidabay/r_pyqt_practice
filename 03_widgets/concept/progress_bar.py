#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QProgressBar, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QProgressBar")
        self.resize(350, 150)
        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        start = QPushButton("Start Progress")
        reset = QPushButton("Reset")
        self.timer = QTimer()
        self.timer.timeout.connect(self._tick)
        start.clicked.connect(lambda: (self.progress.reset(), self.timer.start(50)))
        reset.clicked.connect(lambda: (self.timer.stop(), self.progress.reset()))
        layout = QVBoxLayout()
        layout.addWidget(self.progress)
        layout.addWidget(start)
        layout.addWidget(reset)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def _tick(self):
        val = self.progress.value() + 1
        self.progress.setValue(val)
        if val >= 100:
            self.timer.stop()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
