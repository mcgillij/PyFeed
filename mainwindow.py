# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(584, 411)
        MainWindow.setAutoFillBackground(False)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionFilters = QAction(MainWindow)
        self.actionFilters.setObjectName(u"actionFilters")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.listWidgetRss = QListWidget(self.centralwidget)
        self.listWidgetRss.setObjectName(u"listWidgetRss")
        self.listWidgetRss.setMouseTracking(True)
        self.listWidgetRss.setAlternatingRowColors(True)

        self.gridLayout.addWidget(self.listWidgetRss, 2, 0, 1, 1)

        self.pushRefreshButton = QPushButton(self.centralwidget)
        self.pushRefreshButton.setObjectName(u"pushRefreshButton")

        self.gridLayout.addWidget(self.pushRefreshButton, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 584, 21))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionSettings)
        self.menuMenu.addAction(self.actionFilters)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"FeedPy", None)
        )
        # if QT_CONFIG(tooltip)
        MainWindow.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                u'<html><head/><body><p><span style=" font-size:12pt;">Mouse over any entries in the main list to see a quick summary, or click the item to launch a browser.</span></p></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionSettings.setText(
            QCoreApplication.translate("MainWindow", u"Settings", None)
        )
        self.actionFilters.setText(
            QCoreApplication.translate("MainWindow", u"Filters", None)
        )
        self.pushRefreshButton.setText(
            QCoreApplication.translate("MainWindow", u"Refresh Feeds", None)
        )
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))

    # retranslateUi
