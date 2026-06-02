#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tree Model"); self.resize(350, 250)
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Name", "Role"])
        root = model.invisibleRootItem()
        devs = QStandardItem("Developers")
        devs.appendRow([QStandardItem("Alice"), QStandardItem("Senior")])
        devs.appendRow([QStandardItem("Bob"), QStandardItem("Junior")])
        root.appendRow(devs)
        tree = QTreeView(); tree.setModel(model); tree.expandAll()
        self.setCentralWidget(tree)

app = QApplication(sys.argv); w = MainWindow(); w.show(); sys.exit(app.exec())
