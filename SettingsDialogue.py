""" Dialogue for entering user settings into the app """
import sys
import diag
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Settings import Settings


class SettingsDialogue(QDialog, diag.Ui_Dialog):
    """this should pop up a settings window"""

    def __init__(self, settings, parent=None):
        super(SettingsDialogue, self).__init__(parent)
        self.setupUi(self)
        self.pushAddButton.clicked.connect(self._slotAddClicked)
        self.settings = settings
        self.settings.load_settings()
        self.lineEditRefresh.setText(str(self.settings.refresh_time))
        self.lineEditAlertAt.setText(str(self.settings.alert_time))
        for u in self.settings.uri_list:
            self.listWidgetUrls.addItem(QListWidgetItem(u))
        self.listWidgetUrls.itemClicked.connect(self._slotItemClicked)
        self.lineEditUrl.setFocus()

    def _slotItemClicked(self):
        """clicked on an item in the list widget"""
        item = self.listWidgetUrls.takeItem(self.listWidgetUrls.currentRow())
        item = None

    def _slotAddClicked(self):
        """clicked on the add button"""
        text = self.lineEditUrl.text()
        self.listWidgetUrls.addItem(QListWidgetItem(text))
        text = str(text)
        self.settings.uri_list.append(text)
        self.lineEditUrl.clear()

    def accept(self, *args, **kwargs):
        """Runs when the OK button is pressed and exits the dialogue"""
        self.settings.refresh_time = int(self.lineEditRefresh.text())
        self.settings.alert_time = int(self.lineEditAlertAt.text())
        self.settings.uri_list = []
        items = self.return_items()
        for i in items:
            item_text = str(i.text()).strip()
            if item_text == "":
                pass
            else:
                self.settings.uri_list.append(str(i.text()))
        self.settings.save_settings()
        return QDialog.accept(self, *args, **kwargs)

    def return_items(self):
        """Fetch all the items in the list widget"""
        for i in range(self.listWidgetUrls.count()):
            yield self.listWidgetUrls.item(i)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MA = SettingsDialogue()
    MA.show()
    app.exec_()
