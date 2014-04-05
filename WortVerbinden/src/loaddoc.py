'''
Created on Apr 4, 2014

@author: phoenix
'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loaddoc.ui'
#
# Created: Fri Apr  4 13:28:51 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!
#This is MyPaint
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class LoadDocWin(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphDocView = QtGui.QGraphicsView(self.centralwidget)
        self.graphDocView.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.graphDocView.setObjectName(_fromUtf8("graphDocView"))
        self.labCutPreview = QtGui.QLabel(self.centralwidget)
        self.labCutPreview.setGeometry(QtCore.QRect(720, 510, 71, 81))
        self.labCutPreview.setObjectName(_fromUtf8("labCutPreview"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Select your glyphs", None))
        self.labCutPreview.setText(_translate("MainWindow", "TextLabel", None))

