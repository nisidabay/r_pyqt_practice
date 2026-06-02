#!/usr/bin/env python3
"""Theme Switcher — Toggle between light, dark, and Fusion with a widget gallery."""
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt

DARK_PALETTE = {
    QPalette.ColorRole.Window: QColor(40, 40, 40),
    QPalette.ColorRole.WindowText: QColor(220, 220, 220),
    QPalette.ColorRole.Base: QColor(30, 30, 30),
    QPalette.ColorRole.Text: QColor(220, 220, 220),
    QPalette.ColorRole.Button: QColor(55, 55, 55),
    QPalette.ColorRole.ButtonText: QColor(220, 220, 220),
    QPalette.ColorRole.Highlight: QColor(42, 130, 218),
}

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Theme Switcher"); self.resize(450, 380)
        main = QVBoxLayout()
        theme_combo = QComboBox()
        theme_combo.addItems(["Fusion (Light)", "Fusion (Dark)", "Windows"])
        theme_combo.currentIndexChanged.connect(self._switch_theme)
        main.addWidget(QLabel("Theme:"))
        main.addWidget(theme_combo)
        gb = QGroupBox("Widget Gallery")
        gl = QFormLayout(gb)
        gl.addRow("Name:", QLineEdit("Carlos"))
        gl.addRow("Email:", QLineEdit("carlos@example.com"))
        gl.addRow("Age:", QSpinBox(value=30))
        gl.addRow("Language:", QComboBox())
        gl.addRow("Subscribe:", QCheckBox("Newsletter"))
        gl.addRow(QPushButton("Submit"))
        bar = QProgressBar(); bar.setValue(72)
        gl.addRow("Progress:", bar)
        main.addWidget(gb)
        c = QWidget(); c.setLayout(main); self.setCentralWidget(c)

    def _switch_theme(self, idx):
        if idx == 0:  # Fusion light
            app.setStyle("Fusion")
            app.setPalette(QApplication.style().standardPalette())
        elif idx == 1:  # Fusion dark
            app.setStyle("Fusion")
            p = QPalette()
            for role, color in DARK_PALETTE.items(): p.setColor(role, color)
            app.setPalette(p)
        elif idx == 2:  # Windows
            app.setStyle("Windows")
            app.setPalette(QApplication.style().standardPalette())

app = QApplication(sys.argv)
window = MainWindow(); window.show(); sys.exit(app.exec())
