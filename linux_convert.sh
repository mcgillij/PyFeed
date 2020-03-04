#!/bin/bash
pyside2-rcc feedpy_rc.qrc > feedpy_rc.py
pyside2-uic diag.ui -o diag.py
pyside2-uic mainwindow.ui -o mainwindow.py
pyside2-uic filters.ui -o filters.py

