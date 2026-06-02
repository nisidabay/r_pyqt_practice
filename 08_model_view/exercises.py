#!/usr/bin/env python3
"""Exercises: Model/View practice. Run me: python3 exercises.py"""
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QTimer

app = QApplication(sys.argv)

# === Ex 1: Static table ===
class Ex1(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle("Static Table"); self.resize(350, 200)
        t = QTableWidget(3, 2)
        t.setHorizontalHeaderLabels(["Name", "Score"])
        for r, (n, s) in enumerate([("Alice", "95"), ("Bob", "87"), ("Carol", "92")]):
            t.setItem(r, 0, QTableWidgetItem(n)); t.setItem(r, 1, QTableWidgetItem(s))
        self.setCentralWidget(t)
w1 = Ex1(); w1.show()
print("Ex1: Static table with 3 rows")
QTimer.singleShot(1500, w1.close)
while w1.isVisible(): app.processEvents()
print("-" * 40)

# === Ex 2: Editable table ===
class Ex2(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle("Editable Table"); self.resize(350, 200)
        self.data = [{"name":"Alice","role":"Dev"}, {"name":"Bob","role":"Design"}]
        self.t = QTableWidget(len(self.data), 2)
        self.t.setHorizontalHeaderLabels(["Name", "Role"])
        self._refresh()
        self.t.itemChanged.connect(lambda item: self.data[item.row()].update(
            {["name","role"][item.column()]: item.text()}))
        btn = QPushButton("Show"); btn.clicked.connect(lambda: print(self.data))
        l = QVBoxLayout(); l.addWidget(self.t); l.addWidget(btn)
        c = QWidget(); c.setLayout(l); self.setCentralWidget(c)
    def _refresh(self):
        for r, row in enumerate(self.data):
            self.t.setItem(r, 0, QTableWidgetItem(row["name"]))
            self.t.setItem(r, 1, QTableWidgetItem(row["role"]))
w2 = Ex2(); w2.show()
print("Ex2: Editable table — change cells, click Show")
QTimer.singleShot(2500, w2.close)
while w2.isVisible(): app.processEvents()
print(f"  Data: {w2.data}"); print("-" * 40)

# === Ex 3: Tree widget ===
class Ex3(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle("Tree"); self.resize(300, 200)
        tree = QTreeWidget(); tree.setHeaderLabels(["Item", "Count"])
        books = QTreeWidgetItem(tree, ["Books", "3"])
        QTreeWidgetItem(books, ["Fiction", "2"]); QTreeWidgetItem(books, ["Non-fiction", "1"])
        tools = QTreeWidgetItem(tree, ["Tools", "2"])
        QTreeWidgetItem(tools, ["Hammer", "1"]); QTreeWidgetItem(tools, ["Saw", "1"])
        self.setCentralWidget(tree)
w3 = Ex3(); w3.show()
print("Ex3: Tree widget")
QTimer.singleShot(1500, w3.close)
while w3.isVisible(): app.processEvents()
print("-" * 40)

# === BONUS: Contact table with filter ===
class Bonus(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle("Contacts"); self.resize(450, 300)
        self.data = [["Alice","555-0101","alice@e.com"], ["Bob","555-0202","bob@e.com"],
                     ["Carol","555-0303","carol@e.com"], ["Dave","555-0404","dave@e.com"]]
        self.model = QStandardItemModel(len(self.data), 3)
        self.model.setHorizontalHeaderLabels(["Name","Phone","Email"])
        self.proxy = QSortFilterProxyModel()
        self.proxy.setSourceModel(self.model)
        self.proxy.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self._load()
        tv = QTableView(); tv.setModel(self.proxy)
        search = QLineEdit(); search.setPlaceholderText("Filter...")
        search.textChanged.connect(self.proxy.setFilterFixedString)
        l = QVBoxLayout(); l.addWidget(search); l.addWidget(tv)
        c = QWidget(); c.setLayout(l); self.setCentralWidget(c)
    def _load(self):
        for r, row in enumerate(self.data):
            for c, val in enumerate(row): self.model.setItem(r, c, QStandardItem(val))
w4 = Bonus(); w4.show()
print("Bonus: Contact table with real-time filter")
QTimer.singleShot(3000, w4.close)
while w4.isVisible(): app.processEvents()
print("\nDone!"); sys.exit()
