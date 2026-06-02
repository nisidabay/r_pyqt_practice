#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTreeWidget"); self.resize(350, 300)
        tree = QTreeWidget()
        tree.setHeaderLabels(["Name", "Type"])
        root = QTreeWidgetItem(tree, ["Animals", "Kingdom"])
        mammals = QTreeWidgetItem(root, ["Mammals", "Class"])
        QTreeWidgetItem(mammals, ["Dog", "Species"])
        QTreeWidgetItem(mammals, ["Cat", "Species"])
        birds = QTreeWidgetItem(root, ["Birds", "Class"])
        QTreeWidgetItem(birds, ["Eagle", "Species"])
        QTreeWidgetItem(birds, ["Penguin", "Species"])
        root.setExpanded(True)
        self.setCentralWidget(tree)

app = QApplication(sys.argv); w = MainWindow(); w.show(); sys.exit(app.exec())
