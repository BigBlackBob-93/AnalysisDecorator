from typing import Any
from PyQt6.QtWidgets import (
    QMainWindow,
    QLabel,
    QPushButton,
    QDoubleSpinBox
)
from config import (
    LEFT,
    ABOVE,
    WIDTH,
    HEIGHT
)


class Object:
    """Class for setting form objects and keeping some important of them.

    Fields: objects: dict | functions: dict | indent: int.
    Methods: __init__() | add_obj(obj: Any, key: str) -> None | set_obj(**kwargs) -> Any |
    increase_indent(index: int = 1) -> None | get_objects() -> dict
    """

    def __init__(self):
        """Initialize all fields.

        Fields:
        objects: dict -- analysis data |
        functions: dict -- type-function |
        indent: int -- horizontal indent between form objects.
        """
        self.objects: dict = {
            'info': [],  # exp: patient's name
            'researches': [],  # exp: hematocrit
            'results': []  # exp: 0.5
        }
        self.functions: dict = {
            QMainWindow: set_form,
            QLabel: set_label,
            QPushButton: set_button,
            QDoubleSpinBox: set_spinbox
        }
        self.indent: int = ABOVE

    def add_obj(self, obj: Any, key: str) -> None:
        """Add object to the objects dict"""
        self.objects.get(key).append(obj)

    def set_obj(self, **kwargs) -> Any:
        """Set form object.

        Keyword arguments:
        object  -- setting object |
        title -- visible part |
        left -- vertical indent between form objects (default config.LEFT) |
        above -- horizontal indent between form objects (default config.ABOVE) |
        case: Any -- text stile indicator for QLable setter (None - italic, Any - bold).

        :return: object: QMainWindow | QLabel | QPushButton | QDoubleSpinBox
        """
        self.functions.get(type(kwargs.get('object')))(**kwargs)
        return kwargs.get('object')

    def increase_indent(self, index: int = 1) -> None:
        """Increase horizontal indent between form objects"""
        self.indent = self.indent + ABOVE * index

    def get_objects(self) -> dict:
        """Return dict of the objects"""
        return self.objects


# --------- setters ---------
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
