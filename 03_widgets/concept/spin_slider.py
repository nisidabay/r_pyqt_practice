#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QSpinBox, QDoubleSpinBox,
                              QSlider, QDial, QVBoxLayout, QWidget, QLabel)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spin & Slider")
        self.resize(350, 300)
        self.label = QLabel("SpinBox: 10  |  Slider: 50  |  Dial: 0")
        spin = QSpinBox()
        spin.setRange(0, 100)
        spin.setValue(10)
        dspin = QDoubleSpinBox()
        dspin.setRange(0.0, 100.0)
        dspin.setSingleStep(0.5)
        dspin.setValue(10.0)
        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setRange(0, 100)
        slider.setValue(50)
        dial = QDial()
        dial.setRange(0, 100)
        def update():
            self.label.setText(
                f"SpinBox: {spin.value()}  |  Double: {dspin.value():.1f}  |  Slider: {slider.value()}  |  Dial: {dial.value()}")
        spin.valueChanged.connect(lambda: (slider.setValue(spin.value()), update()))
        slider.valueChanged.connect(lambda: (spin.setValue(slider.value()), update()))
        dspin.valueChanged.connect(lambda v: update())
        dial.valueChanged.connect(lambda v: update())
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(spin)
        layout.addWidget(dspin)
        layout.addWidget(slider)
        layout.addWidget(dial)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
