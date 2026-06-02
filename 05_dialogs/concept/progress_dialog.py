#!/usr/bin/env python3
import sys, time
from PyQt6.QtWidgets import (QApplication, QMainWindow, QProgressDialog, QPushButton,
                              QVBoxLayout, QWidget, QLabel)
from PyQt6.QtCore import Qt, QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QProgressDialog"); self.resize(300, 150)
        self.label = QLabel("Ready")
        btn = QPushButton("Start Long Operation"); btn.clicked.connect(self._start)
        layout = QVBoxLayout(); layout.addWidget(self.label); layout.addWidget(btn)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)

    def _start(self):
        progress = QProgressDialog("Processing files...", "Cancel", 0, 100, self)
        progress.setWindowModality(Qt.WindowModality.WindowModal)
        progress.setMinimumDuration(0)
        for i in range(101):
            if progress.wasCanceled(): break
            progress.setValue(i)
            QApplication.processEvents()
            time.sleep(0.02)
        self.label.setText("Cancelled" if progress.wasCanceled() else "Complete!")

app = QApplication(sys.argv); window = MainWindow(); window.show(); sys.exit(app.exec())
