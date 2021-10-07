""" Derived class that will hold the feed items """
from PySide2.QtWidgets import QListWidgetItem


class RssListItem(QListWidgetItem):
    """Container class for a feed item"""

    def __init__(self, item, *args, **kwargs):
        super(RssListItem, self).__init__(*args, **kwargs)
        self.feed = item
        self.setText(item["title"])
        self.setToolTip(item["summary"])
