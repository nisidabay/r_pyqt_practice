#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QStringListModel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Model/View"); self.resize(350, 250)
        splitter = QSplitter()
        lv = QListView()
        model = QStringListModel(["Python", "Go", "Rust", "JavaScript", "C++"])
        lv.setModel(model)
        tv = QTableView()
        tv.setModel(model)
        splitter.addWidget(lv); splitter.addWidget(tv)
        self.setCentralWidget(splitter)

app = QApplication(sys.argv); w = MainWindow(); w.show(); sys.exit(app.exec())
