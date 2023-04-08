from typing import Any
from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QDoubleSpinBox
from config import (
    LEFT,
    ABOVE,
    WIDTH,
    HEIGHT
)


class Object:
    def __init__(self):
        self.objects = {
            'analysis': [],
            'researches': [],
            'results': []
        }
        self.functions = {
            QMainWindow: set_form,
            QLabel: set_label,
            QPushButton: set_button,
            QDoubleSpinBox: set_spinbox
        }

    def add_obj(self, obj: Any, key: str = 'researches'):
        self.objects.get(key).append(obj)

    def set_obj(self, **kwargs):
        self.functions.get(type(kwargs.get('object')))(**kwargs)


def set_form(**kwargs) -> None:
    form = kwargs.get('object')
    form.setWindowTitle(kwargs.get('title'))
    form.setGeometry(350, 300, WIDTH, HEIGHT)


def set_spinbox(**kwargs) -> None:
    spin_box = kwargs.get('object')
    left = kwargs.get('left') if kwargs.get('left') is not None else LEFT
    above = kwargs.get('above') if kwargs.get('above') is not None else ABOVE

    spin_box.setValue(0)
    spin_box.setFixedSize(60, 20)
    spin_box.setRange(0, 100)
    spin_box.setSingleStep(1)
    spin_box.move(left, above)


def set_label(**kwargs) -> None:
    label = kwargs.get('object')
    title = kwargs.get('title')
    left = kwargs.get('left') if kwargs.get('left') is not None else LEFT
    above = kwargs.get('above') if kwargs.get('above') is not None else ABOVE

    font = label.font()
    font.setPointSize(10)
    label.setFont(font)
    label.setFixedWidth(WIDTH)

    if kwargs.get('case') is None:
        label.setText(title.upper())
    else:
        font.setItalic(True)
        label.setFont(font)
        label.setText(title)
    label.move(left, above)


def set_button(**kwargs) -> None:
    button = kwargs.get('object')
    title = kwargs.get('title')
    left = kwargs.get('left') if kwargs.get('left') is not None else LEFT
    above = kwargs.get('above') if kwargs.get('above') is not None else ABOVE

    button.setText(title.upper())
    button.move(left, above)

