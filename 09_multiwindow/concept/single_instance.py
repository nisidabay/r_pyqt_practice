#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QSharedMemory

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Single Instance"); self.resize(300, 200)
        self.setCentralWidget(QLabel("Only one instance of this app can run.\nTry launching it twice."))

def main():
    app = QApplication(sys.argv)
    shared = QSharedMemory("SingleInstanceApp")
    if not shared.create(1):
        QMessageBox.warning(None, "Already Running", "This application is already running.")
        return
    w = MainWindow(); w.show()
    sys.exit(app.exec())

if __name__ == "__main__": main()
