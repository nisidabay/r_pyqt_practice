#!/usr/bin/env python3
"""What happens when you block the event loop — the UI freezes completely."""
import sys, time
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Blocking Demo"); self.resize(350, 200)
        self.label = QLabel("Click 'Freeze' — UI locks for 5 seconds")
        self.freeze_btn = QPushButton("Freeze (5s)")
        self.freeze_btn.clicked.connect(self._freeze)
        self.test_btn = QPushButton("Try clicking me during freeze")
        self.test_btn.clicked.connect(lambda: self.label.setText("You clicked me!"))
        layout = QVBoxLayout()
        layout.addWidget(self.label); layout.addWidget(self.freeze_btn); layout.addWidget(self.test_btn)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)

    def _freeze(self):
        self.label.setText("FROZEN..."); self.freeze_btn.setEnabled(False)
        time.sleep(5)
        self.label.setText("Unfrozen! UI responds again."); self.freeze_btn.setEnabled(True)

app = QApplication(sys.argv); w = MainWindow(); w.show(); sys.exit(app.exec())
