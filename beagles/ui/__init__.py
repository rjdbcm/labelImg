from math import sqrt
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QPointF
from PyQt5.QtWidgets import QPushButton, QAction, QMenu


class Struct(object):

    def __init__(self, **kwargs):
        """Updates `self.__dict__` with `**kwargs`."""
        self.__dict__.update(kwargs)

    def __repr__(self):
        """
        Returns: `str(self.__dict__)`
        """
        return str(self.__dict__)

    def __ior__(self, other):
        """Merges :obj:`self.__dict__` and :obj:`other.__dict__` using the | operator"""
        self.__dict__ = {**self.__dict__, **other.__dict__}


def newIcon(icon: str):
    return QIcon(':/' + icon)


def newButton(text: str, icon: str = None, slot=None):
    b = QPushButton(text)
    if icon is not None:
        b.setIcon(newIcon(icon))
    if slot is not None:
        b.clicked.connect(slot)
    return b


def newAction(parent, text, slot=None, shortcut=None, icon=None,
              tip=None, checkable=False, enabled=True):
    """Create a new action and assign callbacks, shortcuts, etc."""
    a = QAction(text, parent)
    if icon is not None:
        a.setIcon(newIcon(icon))
    if shortcut is not None:
        if isinstance(shortcut, (list, tuple)):
            a.setShortcuts(shortcut)
        else:
            a.setShortcut(shortcut)
    if tip is not None:
        a.setToolTip(tip)
        a.setStatusTip(tip)
    if slot is not None:
        a.triggered.connect(slot)
    if checkable:
        a.setCheckable(True)
    a.setEnabled(enabled)
    return a


def addActions(widget, actions):
    for action in actions:
        if action is None:
            widget.addSeparator()
        elif isinstance(action, QMenu):
            widget.addMenu(action)
        else:
            widget.addAction(action)


def distance(p: QPointF) -> float:
    """
    Returns:
        Distance from the origin (0,0).
    """
    return sqrt(p.x()**2 + p.y()**2)