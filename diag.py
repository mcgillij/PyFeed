# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diag.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.ApplicationModal)
        Dialog.resize(537, 376)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.listWidgetUrls = QListWidget(Dialog)
        self.listWidgetUrls.setObjectName(u"listWidgetUrls")

        self.gridLayout.addWidget(self.listWidgetUrls, 2, 0, 1, 2)

        self.pushAddButton = QPushButton(Dialog)
        self.pushAddButton.setObjectName(u"pushAddButton")
        self.pushAddButton.setMaximumSize(QSize(40, 16777215))

        self.gridLayout.addWidget(self.pushAddButton, 1, 3, 1, 1)

        self.lineEditUrl = QLineEdit(Dialog)
        self.lineEditUrl.setObjectName(u"lineEditUrl")

        self.gridLayout.addWidget(self.lineEditUrl, 1, 0, 1, 2)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(100, 30))

        self.gridLayout.addWidget(self.label_2, 2, 3, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.lineEditRefresh = QLineEdit(Dialog)
        self.lineEditRefresh.setObjectName(u"lineEditRefresh")
        self.lineEditRefresh.setMaximumSize(QSize(25, 16777215))
        self.lineEditRefresh.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhFormattedNumbersOnly|Qt.ImhPreferNumbers)

        self.gridLayout.addWidget(self.lineEditRefresh, 4, 1, 1, 1)

        self.lineEditAlertAt = QLineEdit(Dialog)
        self.lineEditAlertAt.setObjectName(u"lineEditAlertAt")
        self.lineEditAlertAt.setMaximumSize(QSize(25, 16777215))
        self.lineEditAlertAt.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhFormattedNumbersOnly|Qt.ImhPreferNumbers)

        self.gridLayout.addWidget(self.lineEditAlertAt, 5, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 6, 1, 1, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 3, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Settings", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Alert every (Minutes):", None))
        self.pushAddButton.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"RSS url to add to monitoring:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Click item to remove", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Refresh (Minutes): ", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"0 for Off", None))
    # retranslateUi

