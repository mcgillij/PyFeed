# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filters.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.ApplicationModal)
        Dialog.resize(437, 346)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.listWidgetFilter = QListWidget(Dialog)
        self.listWidgetFilter.setObjectName(u"listWidgetFilter")

        self.gridLayout.addWidget(self.listWidgetFilter, 2, 1, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 3, 1, 1, 1)

        self.lineEditFilter = QLineEdit(Dialog)
        self.lineEditFilter.setObjectName(u"lineEditFilter")
        self.lineEditFilter.setInputMethodHints(Qt.ImhUrlCharactersOnly)

        self.gridLayout.addWidget(self.lineEditFilter, 0, 1, 1, 1)

        self.pushButtonPlus = QPushButton(Dialog)
        self.pushButtonPlus.setObjectName(u"pushButtonPlus")
        self.pushButtonPlus.setMaximumSize(QSize(20, 20))
        self.pushButtonPlus.setInputMethodHints(Qt.ImhNone)

        self.gridLayout.addWidget(self.pushButtonPlus, 0, 2, 1, 1)

        self.pushButtonMinus = QPushButton(Dialog)
        self.pushButtonMinus.setObjectName(u"pushButtonMinus")
        self.pushButtonMinus.setMaximumSize(QSize(20, 20))

        self.gridLayout.addWidget(self.pushButtonMinus, 0, 3, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Filters", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Filter:", None))
        self.pushButtonPlus.setText(QCoreApplication.translate("Dialog", u"+", None))
        self.pushButtonMinus.setText(QCoreApplication.translate("Dialog", u"-", None))
        self.label_2.setText(
            QCoreApplication.translate("Dialog", u"Click to remove item.", None)
        )

    # retranslateUi
