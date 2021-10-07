""" Derived class that will hold the filter items """
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QListWidgetItem


class FilterListItem(QListWidgetItem):
    """Container class for a feed item"""

    def __init__(self, value, plus, *args, **kwargs):
        super(FilterListItem, self).__init__(*args, **kwargs)
        self.setText(value)
        self.value = value
        self.plus = plus
        if self.plus:
            self.setBackgroundColor(Qt.green)
        else:
            self.setBackgroundColor(Qt.red)
