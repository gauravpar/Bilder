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
from PyQt4.Qt import QGraphicsScene, QImage, QGraphicsPixmapItem
from Schkini import Schkini

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

class LoadDocWin(QtGui.QMainWindow):
    DocImagePath=""
    BackFolder=''
    sc=''
    
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1179, 672)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphDocView = QtGui.QGraphicsView(self.centralwidget)
        self.graphDocView.setGeometry(QtCore.QRect(10, 10, 1161, 651))
        self.graphDocView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.graphDocView.setMouseTracking(True)
        self.graphDocView.setFrameShape(QtGui.QFrame.NoFrame)
        self.graphDocView.setObjectName(_fromUtf8("graphDocView"))
        self.comboMode = QtGui.QComboBox(self.centralwidget)
        self.comboMode.setGeometry(QtCore.QRect(997, 620, 121, 23))
        self.comboMode.setObjectName(_fromUtf8("comboMode"))
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.comboMode.addItem("Glyph Cutter") # Mode 0
        self.comboMode.addItem("Area Cutter") # Mode 1
        
        
        #Slots
        self.comboMode.currentIndexChanged.connect(self.ChangeMode)

        print 'Dok path',self.DocImagePath
        self.sc=Schkini()
        self.sc.TmpFolder=self.BackFolder
        img=QImage(self.DocImagePath)
        self.sc.DocImagePath=self.DocImagePath
       
        pix=QGraphicsPixmapItem(QtGui.QPixmap.fromImage(img))
        self.sc.addItem(pix)
        self.graphDocView.setScene(self.sc)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Select your glyphs", None))

    def ChangeMode(self):
        if "Area" in self.comboMode.currentText():
            self.sc.Mode=1
        else:
            self.sc.Mode=0
                
        print 'mode',self.sc.Mode