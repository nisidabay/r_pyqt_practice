#!/usr/bin/env python3
"""Contact Book — JSON-backed contact manager with table view and CRUD."""
import sys, json
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QSortFilterProxyModel
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from pathlib import Path

DB_PATH = Path(__file__).parent / "contacts.json"
DEFAULT = [{"name": "Alice", "phone": "555-0101", "email": "alice@example.com"},
           {"name": "Bob", "phone": "555-0202", "email": "bob@example.com"}]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contact Book"); self.resize(550, 400)
        self.contacts = self._load()
        self.model = QStandardItemModel(len(self.contacts), 3)
        self.model.setHorizontalHeaderLabels(["Name", "Phone", "Email"])
        self.proxy = QSortFilterProxyModel()
        self.proxy.setSourceModel(self.model)
        self.proxy.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self._refresh_model()
        self.tv = QTableView()
        self.tv.setModel(self.proxy)
        self.tv.setSortingEnabled(True)
        self.tv.resizeColumnsToContents()
        search = QLineEdit(); search.setPlaceholderText("Filter contacts...")
        search.textChanged.connect(self.proxy.setFilterFixedString)
        btn_row = QHBoxLayout()
        for text, slot in [("Add", self._add), ("Delete", self._delete)]:
            b = QPushButton(text); b.clicked.connect(slot); btn_row.addWidget(b)
        layout = QVBoxLayout(); layout.addWidget(search)
        layout.addWidget(self.tv); layout.addLayout(btn_row)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)
        sb = QStatusBar(); self.setStatusBar(sb)
        sb.showMessage(f"{len(self.contacts)} contacts loaded")

    def _load(self):
        if DB_PATH.exists():
            return json.loads(DB_PATH.read_text())
        DB_PATH.write_text(json.dumps(DEFAULT, indent=2))
        return DEFAULT.copy()

    def _save(self):
        DB_PATH.write_text(json.dumps(self.contacts, indent=2))

    def _refresh_model(self):
        self.model.removeRows(0, self.model.rowCount())
        self.model.setRowCount(len(self.contacts))
        for r, c in enumerate(self.contacts):
            self.model.setItem(r, 0, QStandardItem(c["name"]))
            self.model.setItem(r, 1, QStandardItem(c["phone"]))
            self.model.setItem(r, 2, QStandardItem(c["email"]))

    def _add(self):
        name, ok = QInputDialog.getText(self, "Add", "Name:")
        if not ok or not name.strip(): return
        phone, ok = QInputDialog.getText(self, "Add", "Phone:")
        if not ok: return
        email, ok = QInputDialog.getText(self, "Add", "Email:")
        if not ok: return
        self.contacts.append({"name": name.strip(), "phone": phone, "email": email})
        self._save(); self._refresh_model()
        self.statusBar().showMessage(f"Added {name.strip()}")

    def _delete(self):
        idx = self.tv.currentIndex()
        if idx.row() < 0:
            QMessageBox.information(self, "Delete", "Select a contact first.")
            return
        src_idx = self.proxy.mapToSource(idx)
        contact = self.contacts[src_idx.row()]
        r = QMessageBox.question(self, "Delete", f"Delete {contact['name']}?")
        if r == QMessageBox.StandardButton.Yes:
            self.contacts.pop(src_idx.row())
            self._save(); self._refresh_model()
            self.statusBar().showMessage(f"Deleted {contact['name']}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow(); w.show()
    sys.exit(app.exec())
