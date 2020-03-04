""" Dialogue for entering filters into the app """
import filters
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Settings import Settings
from FilterListItem import FilterListItem

class FilterDialogue(QDialog, filters.Ui_Dialog):
    """ this should pop up a dialogue window to enter filters
    filters can be + or -, meaning inclusive / exclusive
    """
    def __init__(self, settings, parent=None):
        super(FilterDialogue, self).__init__(parent)
        self.setupUi(self)
        self.pushButtonPlus.setDefault(True)
        self.pushButtonPlus.clicked.connect(self._slotPlusClicked)
        self.pushButtonMinus.clicked.connect(self._slotMinusClicked)
        self.settings = settings
        self.settings.load_settings()
        for f in self.settings.filters:
            self.listWidgetFilter.addItem(FilterListItem(f['filter'], f['plus']))
        self.listWidgetFilter.itemClicked.connect(self._slotItemClicked)
        self.lineEditFilter.setFocus()

    def _slotItemClicked(self):
        """ clicked on an item in the list widget """
        item = self.listWidgetFilter.takeItem(self.listWidgetFilter.currentRow())
        item = None

    def _slotPlusClicked(self):
        """ clicked on the add button """
        text = self.lineEditFilter.text()
        plus = True
        item = FilterListItem(text, plus)
        self.listWidgetFilter.addItem(item)
        self.lineEditFilter.clear()
        
    def _slotMinusClicked(self):
        """ clicked on the add button """
        text = self.lineEditFilter.text()
        plus = False
        item = FilterListItem(text, plus)
        self.listWidgetFilter.addItem(item)
        self.lineEditFilter.clear()

    def accept(self, *args, **kwargs):
        """ Runs when the OK button is pressed and exits the dialogue """
        self.settings.filters = []
        items = self.return_items()
        for i in items:
            item_text = str(i.text()).strip()
            if item_text == '':
                pass
            else:
                self.settings.filters.append({'filter': str(i.value), 'plus': i.plus})
        self.settings.save_settings()
        from pprint import pprint
        return QDialog.accept(self, *args, **kwargs)

    def return_items(self):
        """ Fetch all the items in the list widget """
        for i in range(self.listWidgetFilter.count()):
            yield self.listWidgetFilter.item(i)
        
if __name__=='__main__':
    from Settings import Settings
    settings = Settings()
    app = QApplication(sys.argv)
    MA = FilterDialogue(settings)
    MA.show()
    rc = app.exec_()
    print((str(rc)))
