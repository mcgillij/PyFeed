#!/usr/bin/python
""" main class """
import webbrowser
from PySide2 import QtGui
from PySide2.QtCore import *
from PySide2.QtWidgets import *
import sys
from pprint import pprint
import os, glob
# Import the interface class
import mainwindow 
from FeedReader import FeedReader
from RssListItem import RssListItem
import pickle
from Settings import Settings
from SettingsDialogue import SettingsDialogue
import time
from FilterDialogue import FilterDialogue
import functools
import string
try:
    import feedpy_rc
except:
    print("failed to load your resource")

class MainApp(QMainWindow, mainwindow.Ui_MainWindow):
    """ MainApp Class thats generated from the mainwindow.ui and converted to python """
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        self.makeSysTrayActions()
        self.makeTrayIcon()
        self.systrayIcon.messageClicked.connect(self.messageClicked)
        self.systrayIcon.activated.connect(self.iconActivated)
        self.systray_text_list = []
        self.setIcon()
        self.systrayIcon.show()
        self.feed_reader = FeedReader()
        self.active_filter = None
        self.exclusive_filters = None
        self.settings = Settings()
        self.settings.load_settings()
        self.statusbar.showMessage('Feeds tracked: ' + str(len(self.settings.uri_list)))
        self.actionQuit.triggered.connect(sys.exit)
        self.actionSettings.triggered.connect(self._slotSettings)
        self.actionFilters.triggered.connect(self._slotFilters)
        self.pushRefreshButton.clicked.connect(self._slotRefresh)
        self.listWidgetRss.itemClicked.connect(self._slotItemClicked)
        self.settings_dialogue = SettingsDialogue(self.settings, parent=self)
        self.filter_dialogue = FilterDialogue(self.settings, parent=self)
        self.refresh_timer = QTimer()
        self.refresh_timer.timeout.connect(self._slotRefresh)
        if self.settings.refresh_time != 0:
            self.refresh_timer.start(self.settings.refresh_time * 60 * 1000)
        self.alert_timer = QTimer()
        self.alert_timer.timeout.connect(self._slotAlert)
        if self.settings.alert_time != 0:
            self.alert_timer.start(self.settings.alert_time * 60 * 1000)
        self._slotRefresh()
        #one_off_timer = QTimer()
        #one_off_timer.singleShot(1, self._slotRefresh)
        
    def setVisible(self, visible):
        #self.minimizeAction.setEnabled(visible)
        self.maximizeAction.setEnabled(not self.isMaximized())
        self.restoreAction.setEnabled(self.isMaximized() or not visible)
        super(MainApp, self).setVisible(visible)

    def closeEvent(self, event):
        if self.systrayIcon.isVisible():
            self.hide()
            event.ignore()

    def setIcon(self):
        icon = QtGui.QIcon(":/dorf.png")
        self.systrayIcon.setIcon(icon)
        self.setWindowIcon(icon)

    def iconActivated(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            if super(MainApp, self).isVisible() and self.systrayIcon.isVisible():
                self.hide()
            else:
                self.show()
        elif reason == QSystemTrayIcon.MiddleClick:
            self.showMessage()

    def _slotAlert(self):
        if not super(MainApp, self).isVisible():
            icon = QSystemTrayIcon.MessageIcon()
            duration = 5 * 1000
            text = "\n".join(self.systray_text_list)
            self.systrayIcon.showMessage("FeedPy Alert", text , icon, duration)

    def showMessage(self):
        icon = QSystemTrayIcon.MessageIcon()
        duration = 5 * 1000
        text = "\n".join(self.systray_text_list)
        self.systrayIcon.showMessage("FeedPy Alert", text , icon, duration)

    def messageClicked(self):
        if not super(MainApp, self).isVisible():
            self.show()

    def makeTrayIcon(self):
        self.systrayMenu = QMenu(self)
        self.systrayMenu.addAction(self.maximizeAction)
        self.systrayMenu.addAction(self.restoreAction)
        self.systrayMenu.addSeparator()
        self.systrayMenu.addAction(self.quitAction)
        self.systrayIcon = QSystemTrayIcon(self)
        self.systrayIcon.setContextMenu(self.systrayMenu)

    def makeSysTrayActions(self):
        self.maximizeAction = QAction("Ma&ximize", self, triggered=self.showMaximized)
        self.restoreAction = QAction("&Restore", self, triggered=self.showNormal)
        self.quitAction = QAction("&Quit", self, triggered=sys.exit)
        #self.quitAction = QAction("&Quit", self, triggered=QtGui.QGuiApplication.quit)

    def generate_filter_buttons(self):
        # clear the hbox of widgets before adding new ones.
        self.active_filter = None
        for i in range(self.horizontalLayout.count()):
            self.horizontalLayout.itemAt(i).widget().close()
        exclusive_filters = []
        for f in self.settings.filters:
            if f['plus']:
                num = self.get_filter_count(f)
                widget_text  = f['filter'] + " (" + str(num) + ")"
                widget = QtGui.QPushButton(widget_text)
                widget.clicked.connect(functools.partial(self.filter_on, f))
                self.horizontalLayout.addWidget(widget)
            else:
                exclusive_filters.append(f)
        if exclusive_filters:
            self.exclusive_filters = exclusive_filters
        else:
            self.exclusive_filters = None

    def updateSystrayMessage(self):
        self.systray_text_list = []
        all_entries = len(self.feed_reader.entries)
        text = "All: " + str(all_entries)
        self.systray_text_list.append(text)
        for f in self.settings.filters:
            if f['plus']:
                num = self.get_filter_count(f)
                text = f['filter'] + " (" + str(num) + ")"
                self.systray_text_list.append(text)
        if self.systray_text_list:
            text_string = "\n".join(self.systray_text_list)
            self.systrayIcon.setToolTip(text_string)

    def get_filter_count(self, pattern):
        count = 0
        for entry in self.feed_reader.entries:
            contains = check_for_val(entry, pattern['filter'])
            if contains:
                count = count + 1
        return count

    def filter_on(self, pattern):
        self.active_filter = pattern
        temp_list = []
        self.listWidgetRss.clear()
        for entry in self.feed_reader.entries:
            contains = check_for_val(entry, pattern['filter'])
            if contains:
                temp_list.append(entry)
        temp_list = self.filter_out(temp_list)
        for i in temp_list:
            RssListItem(i, self.listWidgetRss)

    def filter_out(self, mylist):
        if self.exclusive_filters:
            temp_list = []
            for entry in mylist:
                flagged = False
                for pattern in self.exclusive_filters:
                    contains = check_for_val(entry, pattern['filter'])
                    if contains:
                        flagged = True
                if not flagged:
                    temp_list.append(entry)
            return temp_list
        else: 
            return mylist

    def _slotFilters(self):
        return_value = self.filter_dialogue.exec_()
        if return_value == 1:
            self.settings.load_settings()
            self.generate_filter_buttons()

    def _slotSettings(self):
        """ Clicked on the settings menu item """
        return_value = self.settings_dialogue.exec_()
        if return_value == 1:
            self.settings.load_settings()
            self.refresh_timer.stop()
            if self.settings.refresh_time != 0:
                self.refresh_timer.start(self.settings.refresh_time * 60 * 1000)
            self.alert_timer.stop()
            if self.settings.alert_time != 0:
                self.alert_timer.start(self.settings.alert_time * 60 * 1000)
            self._slotRefresh()
        self.statusbar.showMessage('Feeds tracked: ' + str(len(self.settings.uri_list)))

    def _slotItemClicked(self):
        """ RSS list item clicked"""
        for item in self.listWidgetRss.selectedItems():
            webbrowser.open(item.feed.link)

    def _slotRefresh(self):
        """ Refresh button clicked """
        self.statusbar.showMessage("Refreshing feeds")
        five_hours = 18000
        local_time = time.mktime(time.gmtime())
        start_time = time.time()
        self.statusbar.showMessage("Refreshing feeds")
        self.refresh_timer.stop()
        self.listWidgetRss.clear()
        self.feed_reader.parse(self.settings.uri_list)
        temp_list = self.feed_reader.entries[:]
        temp_list = self.filter_out(temp_list)
        has_time = False
        for entry in temp_list:
            item = RssListItem(entry, self.listWidgetRss)
            if 'published_parsed' in item.feed:
                mytime = time.mktime(item.feed['published_parsed'])
                has_time = True
            elif 'updated_parsed' in item.feed:
                mytime = time.mktime(item.feed['updated_parsed'])
                has_time = True
            if has_time:
                has_time = False
                difference = local_time - mytime
                difference = int(difference)
                if difference < five_hours:
                    item.setBackgroundColor(Qt.green)
        if self.settings.refresh_time != 0:
            self.refresh_timer.start(self.settings.refresh_time * 60 * 1000)
        status_string = "Refresh took: " + str(int((time.time()- start_time))) + " seconds."
        self.statusbar.showMessage(status_string, 2000)
        self.updateSystrayMessage()

    def main(self):
        self.show()

def check_for_val(entry, pattern):
    for key, value in list(entry.items()):
        if isinstance(value, dict):
            continue
        else:
            try:
                value = str(value).encode('utf-8')
                result = value.lower().find(pattern.lower())
                if result != -1:    
                    return True
            except UnicodeEncodeError:
                pass
    return False

def is_ascii(s):
    s = str(s)
    for c in s:
        if c not in string.ascii_letters:
            return False
    return True

if __name__=='__main__':
    app = QApplication(sys.argv)
    MA = MainApp()
    MA.main()
    app.setStyle("plastique")
    app.exec_()
