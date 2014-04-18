# -*- coding: UTF-8 -*- 
import sys


from loaddoc import LoadDocWin
from PyQt4 import QtCore, QtGui
from Glyph import GlyphElement
from PyQt4.QtSql import *
from PyQt4.Qt import QListWidgetItem
from PyQt4.QtGui import QPixmap
from Bildmaschine import BildMaschine
import numpy as np
import cv2


#SELECT *  FROM `Chars` WHERE BINARY `Text` = 'ὠ'

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

class Ui_MainWindow(object):
    GlyphBook=[] # Hier  stehen die Buchstaben und ihre Bilder It is a list of Glyph  instances
    
    
    BackFolder='/home/phoenix/Desktop/buchbilder/' #The backup folder
    #We ll use this instead of xml
    
    
    Norm_Methods=['Slant','Skew','Whitespace','Baseline','Word Height']
    ComboList=[]
    
    Glyph_Chars=[] #Distinct query chars
    Sprache=''
    vasi = QSqlDatabase.addDatabase("QMYSQL");
    
    MainEngine=BildMaschine('','')

        
    SelectedChar=''
  
  
    SessionsFile=BackFolder+"sess"
  
  
    def UpdateTable(self):
        #print 'Updating List widget'
        #clear table and create as many columns as the distinct characters
        
        #print 'Distinct characters in query'
        
        temp=QtCore.QString().fromUtf8(self.textQuery.toPlainText())
        self.Glyph_Chars=[]
        for char in temp:
            #skip empty space and enter aka escape char
            if "\n" not in char and " " not in char and char not in self.Glyph_Chars: # to glyph car periexei tous diakritous xaraktires
                
                self.Glyph_Chars.append(char)
                     
        #populate listwidget GlypWidget
        self.glyphWidget.clear();
        #Color should be red that mean's no grapheme has been choosed
        for char in self.Glyph_Chars:
            charListItem=QtGui.QListWidgetItem()
            charListItem.setText(char)
            self.glyphWidget.addItem(charListItem)
            found=0
            for gl in self.GlyphBook:
                if gl.Char in char:
                    found=1
                    
            if found==0:
                charListItem.setTextColor(QtCore.Qt.red)
            else:
                charListItem.setTextColor(QtCore.Qt.blue)
                
          
    
        
       
    def Go(self):
        print 'Order of normalization'
        for c in self.ComboList:
            print c.currentText()
        self.MainEngine.Query=self.textQuery.toPlainText()
        self.MainEngine.BilderBuch=self.GlyphBook
        self.MainEngine.Anfangen()
        
        
        
    #GUI SUTFF DO NOT CHANGE
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(823, 657)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(22, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 19, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 145, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 255, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 7, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 155, 11))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(174, 10, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 145, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 140, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 19, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 145, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 255, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 7, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 155, 11))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(174, 10, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 145, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 140, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(144, 141, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 19, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(169, 167, 167))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 147, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 7, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(205, 200, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(174, 10, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 145, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 140, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 801, 611))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.textQuery = QtGui.QTextEdit(self.groupBox)
        self.textQuery.setGeometry(QtCore.QRect(10, 30, 761, 31))
        self.textQuery.setObjectName(_fromUtf8("textQuery"))
        self.pushGo = QtGui.QPushButton(self.centralwidget)
        self.pushGo.setGeometry(QtCore.QRect(670, 80, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushGo.setFont(font)
        self.pushGo.setObjectName(_fromUtf8("pushGo"))
        self.pushLoad = QtGui.QPushButton(self.centralwidget)
        self.pushLoad.setGeometry(QtCore.QRect(518, 80, 141, 31))
        self.pushLoad.setObjectName(_fromUtf8("pushLoad"))
        self.tabWidget_2 = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(20, 130, 241, 511))
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.labGlyhPreview = QtGui.QLabel(self.tab_3)
        self.labGlyhPreview.setGeometry(QtCore.QRect(70, 330, 91, 91))
        self.labGlyhPreview.setObjectName(_fromUtf8("labGlyhPreview"))
        self.pushReplace = QtGui.QPushButton(self.tab_3)
        self.pushReplace.setGeometry(QtCore.QRect(60, 430, 99, 31))
        self.pushReplace.setObjectName(_fromUtf8("pushReplace"))
        self.glyphWidget = QtGui.QListWidget(self.tab_3)
        self.glyphWidget.setGeometry(QtCore.QRect(10, 10, 201, 301))
        self.glyphWidget.setObjectName(_fromUtf8("glyphWidget"))
        self.tabWidget_2.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.tab_4)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 201, 441))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.glyphLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.glyphLayout.setMargin(0)
        self.glyphLayout.setObjectName(_fromUtf8("glyphLayout"))
        self.tabWidget_2.addTab(self.tab_4, _fromUtf8(""))
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setObjectName(_fromUtf8("tab_8"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.tab_8)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 201, 461))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.NaherLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.NaherLayout.setMargin(0)
        self.NaherLayout.setObjectName(_fromUtf8("NaherLayout"))
        self.tabWidget_2.addTab(self.tab_8, _fromUtf8(""))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(280, 130, 521, 511))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(58, 23, 174))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 64, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(77, 37, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 75, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 23, 174))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 64, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(77, 37, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 75, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 23, 174))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 64, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(77, 37, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 75, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.tabWidget.setPalette(palette)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabResults = QtGui.QWidget()
        self.tabResults.setObjectName(_fromUtf8("tabResults"))
        self.labFinal = QtGui.QLabel(self.tabResults)
        self.labFinal.setGeometry(QtCore.QRect(10, 10, 501, 161))
        self.labFinal.setObjectName(_fromUtf8("labFinal"))
        self.tabWidget.addTab(self.tabResults, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(40, 10, 81, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineTemp = QtGui.QLineEdit(self.tab_2)
        self.lineTemp.setGeometry(QtCore.QRect(140, 20, 321, 22))
        self.lineTemp.setObjectName(_fromUtf8("lineTemp"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 60, 191, 391))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayoutWidget = QtGui.QWidget(self.groupBox_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 40, 171, 351))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.normLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.normLayout.setMargin(0)
        self.normLayout.setObjectName(_fromUtf8("normLayout"))
        self.pushLoadSession = QtGui.QPushButton(self.tab_2)
        self.pushLoadSession.setGeometry(QtCore.QRect(300, 82, 131, 31))
        self.pushLoadSession.setObjectName(_fromUtf8("pushLoadSession"))
        self.pushSaveSession = QtGui.QPushButton(self.tab_2)
        self.pushSaveSession.setGeometry(QtCore.QRect(300, 130, 131, 31))
        self.pushSaveSession.setObjectName(_fromUtf8("pushSaveSession"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.charWidget = QtGui.QListWidget(self.tab)
        self.charWidget.setGeometry(QtCore.QRect(20, 20, 131, 431))
        self.charWidget.setObjectName(_fromUtf8("charWidget"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(190, 40, 111, 41))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.comboSprache = QtGui.QComboBox(self.tab)
        self.comboSprache.setGeometry(QtCore.QRect(310, 50, 161, 23))
        self.comboSprache.setObjectName(_fromUtf8("comboSprache"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab)
        self.groupBox_4.setGeometry(QtCore.QRect(170, 130, 341, 331))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.laDBGlyph = QtGui.QLabel(self.groupBox_4)
        self.laDBGlyph.setGeometry(QtCore.QRect(100, 110, 141, 131))
        self.laDBGlyph.setObjectName(_fromUtf8("laDBGlyph"))
        self.comboGlyphs = QtGui.QComboBox(self.groupBox_4)
        self.comboGlyphs.setGeometry(QtCore.QRect(150, 50, 141, 23))
        self.comboGlyphs.setObjectName(_fromUtf8("comboGlyphs"))
        self.label_4 = QtGui.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(30, 40, 111, 41))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushUseDBGlyph = QtGui.QPushButton(self.groupBox_4)
        self.pushUseDBGlyph.setGeometry(QtCore.QRect(130, 260, 99, 31))
        self.pushUseDBGlyph.setObjectName(_fromUtf8("pushUseDBGlyph"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.labVorher = QtGui.QLabel(self.tab_5)
        self.labVorher.setGeometry(QtCore.QRect(90, 30, 91, 101))
        self.labVorher.setObjectName(_fromUtf8("labVorher"))
        self.tabWidget_3 = QtGui.QTabWidget(self.tab_5)
        self.tabWidget_3.setGeometry(QtCore.QRect(30, 170, 341, 301))
        self.tabWidget_3.setObjectName(_fromUtf8("tabWidget_3"))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.label_5 = QtGui.QLabel(self.tab_6)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 91, 41))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineKernel = QtGui.QLineEdit(self.tab_6)
        self.lineKernel.setGeometry(QtCore.QRect(120, 20, 61, 22))
        self.lineKernel.setObjectName(_fromUtf8("lineKernel"))
        self.pushErode = QtGui.QPushButton(self.tab_6)
        self.pushErode.setGeometry(QtCore.QRect(10, 220, 99, 31))
        self.pushErode.setObjectName(_fromUtf8("pushErode"))
        self.pushDilate = QtGui.QPushButton(self.tab_6)
        self.pushDilate.setGeometry(QtCore.QRect(220, 220, 99, 31))
        self.pushDilate.setObjectName(_fromUtf8("pushDilate"))
        self.tableKernel = QtGui.QTableWidget(self.tab_6)
        self.tableKernel.setGeometry(QtCore.QRect(70, 50, 181, 141))
        self.tableKernel.setObjectName(_fromUtf8("tableKernel"))
        self.tableKernel.setColumnCount(0)
        self.tableKernel.setRowCount(0)
        self.tabWidget_3.addTab(self.tab_6, _fromUtf8(""))
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        self.horizontalSlider = QtGui.QSlider(self.tab_7)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 80, 281, 23))
        self.horizontalSlider.setMinimum(-20)
        self.horizontalSlider.setMaximum(20)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.tabWidget_3.addTab(self.tab_7, _fromUtf8(""))
        self.labNaher = QtGui.QLabel(self.tab_5)
        self.labNaher.setGeometry(QtCore.QRect(210, 30, 91, 101))
        self.labNaher.setObjectName(_fromUtf8("labNaher"))
        self.listUndo = QtGui.QListWidget(self.tab_5)
        self.listUndo.setGeometry(QtCore.QRect(400, 210, 111, 261))
        self.listUndo.setObjectName(_fromUtf8("listUndo"))
        self.label_6 = QtGui.QLabel(self.tab_5)
        self.label_6.setGeometry(QtCore.QRect(410, 170, 101, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.labHistory = QtGui.QLabel(self.tab_5)
        self.labHistory.setGeometry(QtCore.QRect(320, 30, 91, 101))
        self.labHistory.setObjectName(_fromUtf8("labHistory"))
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)


        
        #BE CAREFUL NOT THE DELETE THESE LINES
        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # My methods-----------------------------------------
      
        
        
        self.lineTemp.setText('/home/phoenix/Desktop/buchbilder/')
        
        self.comboSprache.addItem("EN")
        self.comboSprache.addItem("GR")
        
        self.lineKernel.setText("3")
        
        self.lineTemp.setText(self.BackFolder)
        #combo box with all possible normalization methods
        
        for i in range(0,self.Norm_Methods.__len__()):
            combo=QtGui.QComboBox()
            for n in self.Norm_Methods:
                combo.addItem(n)
                combo.setCurrentIndex(i)
            self.ComboList.append(combo)
            self.normLayout.addWidget(combo)
        self.GetGlyphsFromDB()
        
       
        
        #slots
        QtCore.QObject.connect(self.pushReplace,QtCore.SIGNAL('clicked()'),self.ReplaceGlyph)
        QtCore.QObject.connect(self.pushGo,QtCore.SIGNAL('clicked()'),self.Go)
        QtCore.QObject.connect(self.pushLoad,QtCore.SIGNAL('clicked()'),self.LoadDoc)
        
        QtCore.QObject.connect(self.textQuery,QtCore.SIGNAL('textChanged()'),self.UpdateTable)
        self.charWidget.itemClicked.connect(self.ShowDBGlyph)
        self.glyphWidget.itemClicked.connect(self.ShowDiskGlyph)
        self.charWidget.itemDoubleClicked.connect(self.AppendChar)
        self.comboSprache.currentIndexChanged.connect(self.LangChoice)
        self.pushDilate.clicked.connect(self.Dilate)
        self.pushErode.clicked.connect(self.Erode)
        self.horizontalSlider.valueChanged.connect(self.SliderMoved)
        self.lineKernel.editingFinished.connect(self.CustomKernel)
        self.pushSaveSession.clicked.connect(self.SaveSession)
        
        
        
    def SaveSession(self):
        print('save glyph char s and path to images')
        
        
    
    def SliderMoved(self,value):
        #find the char whose glyph is to be rotated
        for gl in self.GlyphBook:
            if self.SelectedChar in gl.Char:
                print 'Rotate  char',self.SelectedChar,'by',value
                #update the glyphbook!
                gl.Naher=self.MainEngine.Rotate(gl.Naher, value)
                #and the label
                cv2.imwrite(self.BackFolder+str(self.SelectedChar).encode('utf-8') +"_bkp.png",gl.Naher)
                rotpixie=QPixmap(self.BackFolder+str(self.SelectedChar).decode('utf-8') +"_bkp.png")
                self.labNaher.setPixmap(rotpixie)
                #Update History
                gl.History.append(gl.Naher)
                self.FillUndoListWidget(gl.Char)

        self.ShowNaherGlyphs()     



    def CustomKernel(self):
        size=int(self.lineKernel.text())
        print 'Creating a new array',size,'by',size

      
        #tableKernel is a QTableWidget
        
        self.tableKernel.setRowCount(size)
        self.tableKernel.setColumnCount(size)
        
        
        for i in range(0,size):
            self.tableKernel.setColumnWidth(i,28)
            for j in range(0,size):
                itm=QtGui.QTableWidgetItem()
                itm.setText("1")
                self.tableKernel.setItem(i,j,itm)
        
            
        
        
        
        
    def Erode(self):
        self.ErodeDilate('Erode')
        
    def Dilate(self):
        self.ErodeDilate('Dilate')
        
        
        
        
    def GetKernel(self):
        size=int(self.lineKernel.text())
        
        kernel = np.ones((size,size),np.uint8)
          
          
        for i in range(0,size):
            for j in range(0,size):
                kernel[i][j]=int(self.tableKernel.currentItem().
                
        return kernel
    
    
        
    def ErodeDilate(self,index):
        #maybe add an undo action???
        oper=''

        if 'Erode' in index:
            oper='Erod'
        else:
            oper='Dil'
      
        
    
        for gl in self.GlyphBook:
            if self.SelectedChar in gl.Char:
                
                print 'Erosion/Dilation for char',self.SelectedChar
                #update the glyphbook!!!!
                gl.Naher=self.SystolDiastol(oper,  gl.Naher,gl.Char)
                #REDECT LINES
                gl.DetectLines()
                #Update History
                gl.History.append(gl.Naher)
                
                self.FillUndoListWidget(gl.Char)
           
        self.ShowNaherGlyphs()  
       
           
        
        
        
    def SystolDiastol(self,operation,pic_arr,char):
        #Dilate or erosion
        #binarize it
        sysdias=[]
        if operation=='Erod':
            sysdias=self.MainEngine.Erode(pic_arr, self.GetKernel())
        elif operation=='Dil':
            sysdias=self.MainEngine.Dilate(pic_arr, self.GetKernel())
            
        print 'Saving dil/erod to ',self.BackFolder+str(char).encode('utf-8'),'_bkp.png'
        
        cv2.imwrite(self.BackFolder+str(char).encode('utf-8') +"_bkp.png",sysdias)
        #update the label
        erdilpixie=QPixmap(self.BackFolder+str(char).decode('utf-8') +"_bkp.png")
        self.labNaher.setPixmap(erdilpixie)
       
        return sysdias
        
        
        
        
        
    def ShowDiskGlyph(self,item):
        self.labGlyhPreview.clear()
        self.labVorher.clear()
        self.labNaher.clear()
        for gl in self.GlyphBook:
            if gl.Char in item.text():
                self.SelectedChar=item.text()
                print ('Image path for ',item.text(),'is ',gl.GraphemeImg)
                pixie=QPixmap(gl.GraphemeImg)
                self.labGlyhPreview.setPixmap(pixie)
                self.labVorher.setPixmap(pixie)
                
                cv2.imwrite(self.BackFolder + str(gl.Char).encode('utf-8') +".png", gl.Naher)
                pixie=QPixmap(self.BackFolder + str(gl.Char).decode('utf-8') +".png")

                self.labNaher.setPixmap(pixie)
                
                
                
        
    def LoadDoc(self):
        print 'Loading document'
        #Allows the user to load a document
        
        #Finally it works!!!
        self.CutForm = QtGui.QMainWindow()
        self.cui = LoadDocWin()
        self.cui.DocImagePath= unicode(QtGui.QFileDialog.getOpenFileName(None, 'Open File', '', "*.*"))  
        self.cui.BackFolder=self.BackFolder
          
        self.cui.setupUi(self.CutForm)
      
        self.CutForm.show()
        




    def FillUndoListWidget(self,char):
        print 'Showing editing history for',char
        self.listUndo.clear()
        for gl in self.GlyphBook:
            if char in gl.Char:
                for i in range(0,len(gl.History)):
                    it=QtGui.QListWidgetItem()
                    it.setText("Glyph" + str(i))
                    self.listUndo.addItem(it)
                    
    
    def ShowNaherGlyphs(self):
        print 'Showing Naher glyphs'
        
        #clear naherlayout
        for i in reversed(range(self.NaherLayout.count())): 
            self.NaherLayout.itemAt(i).widget().setParent(None)   
        
        for gl in self.GlyphBook:
            lab=QtGui.QLabel()
            
            
            cv2.imwrite(self.BackFolder + str(gl.Char).encode('utf-8') +"naher.png",gl.Naher)

            pix=QPixmap(self.BackFolder + str(gl.Char).decode('utf-8') +"naher.png")
            
            lab.setPixmap(pix)
            
            self.NaherLayout.addWidget(lab)   
             
        
        
    def ShowGlyphFromHistory(self,id):
        print 'Showing history glyph',id
        
        
        
                    
                    
    def ShowSpecificGlyph(self):
        print('#This is called when the comboGlyph current index is changed')
        
        
    def ReplaceGlyph(self):
        item=self.glyphWidget.selectedItems()
        filename = unicode(QtGui.QFileDialog.getOpenFileName(None, 'Select Glyph for '+item[0].text(), '', "*.*"))  
       
        gl=GlyphElement(item[0].text(),filename)
        
        #load the image into Naher and Vorher
        gl.Naher=cv2.imread(filename,cv2.CV_LOAD_IMAGE_GRAYSCALE)
        gl.Vorher=cv2.imread(filename,cv2.CV_LOAD_IMAGE_GRAYSCALE)
       
        #binarize it
        gl.Naher=self.MainEngine.Otsu(gl.Naher)
        gl.Vorher=self.MainEngine.Otsu(gl.Vorher)
        
        
        self.GlyphBook.append(gl)
        
        #update glyphwidget
        for i in reversed(range(self.glyphLayout.count())): 
            self.glyphLayout.itemAt(i).widget().setParent(None)   
        for gl in self.GlyphBook:
            lab=QtGui.QLabel()
            pix=QPixmap(gl.GraphemeImg)
            lab.setPixmap(pix)
            self.glyphLayout.addWidget(lab)   
             
            
            
            
             
    def AppendChar(self,polychar):
        #appends chars to text
        #very useful for polytonic greek characters
        self.textQuery.insertPlainText(polychar.text())
        
    def LangChoice(self,index):
        self.Sprache=self.comboSprache.currentText()
        print 'Language set to ' + self.Sprache
        #update listwidget
        self.GetGlyphsFromDB()
               
               
               
    def ShowDBGlyph(self,item):
        #load the DB glyphs of item
        #English char have many glyphs
        print 'Fetching glyphs for ' + item.text()
        self.comboGlyphs.clear()
        pixie=QtGui.QPixmap()
        self.vasi.open()
        query=QSqlQuery()
        query.prepare("Select Count(Pic) From Glyphs Where CharID IN (SELECT CharID FROM  `Chars` WHERE BINARY `Text` LIKE :char)")
        query.bindValue(":char", item.text())
        query.exec_()
        while (query.next()):
            print 'Glyph count',query.value(0).toString()

            for k in range(1,int(query.value(0).toString())):
                self.comboGlyphs.addItem("Glyph " +str(k))
            
        query.prepare("Select Pic From Glyphs Where CharID IN (SELECT CharID FROM  `Chars` WHERE BINARY `Text` LIKE :char)")
        query.bindValue(":char", item.text())
        query.exec_()
        while (query.next()):
            pixie.loadFromData(query.value(0).toByteArray(),"PNG")
        self.laDBGlyph.setPixmap(pixie)
        
        
        
    def GetGlyphsFromDB(self):
        #fetch greek chars from mysql
        try:
            self.charWidget.clear()
            print 'Reading chars from DB'
            self.vasi.setHostName("localhost")
            self.vasi.setDatabaseName("Kathareyousan")
            self.vasi.setUserName("reichstag")
            self.vasi.setPassword("reichstag")
            self.vasi.open()
            query=QSqlQuery(self.vasi)
            #query.prepare("Select Text From Chars  Where LangID IN (SELECT LangID From Language Where Name=:spr)")
            #query.bindValue(":spr",self.Sprache)
            query.exec_("Select Text From Chars  Where LangID IN (SELECT LangID From Language Where Name='"+self.Sprache+"')")
            
            
            while query.next():
                print query.value(0).toString()
                charListItem=QtGui.QListWidgetItem()
                charListItem.setText(query.value(0).toString())
                charListItem.setTextColor(QtCore.Qt.blue)
                self.charWidget.addItem(charListItem)
            
        except:
            msg=QtGui.QMessageBox()
            msg.setText("Sfalma")
            msg.show()
            
        finally:
            self.vasi.close()
            
        
        
    #GUI SUTFF DO NOT CHANGE
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Buchstabebilderverarbeitungzusammenverbindungsystem", None))
        self.groupBox.setTitle(_translate("MainWindow", "String Query", None))
        self.pushGo.setText(_translate("MainWindow", "GO", None))
        self.pushLoad.setText(_translate("MainWindow", "Load Document", None))
        self.labGlyhPreview.setText(_translate("MainWindow", "TextLabel", None))
        self.pushReplace.setText(_translate("MainWindow", "Use from disk", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Chars", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "All Glyphs", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("MainWindow", "Final Glyphs", None))
        self.labFinal.setText(_translate("MainWindow", "TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabResults), _translate("MainWindow", "Results", None))
        self.label.setText(_translate("MainWindow", "Temp Folder", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Order of Normalization", None))
        self.pushLoadSession.setText(_translate("MainWindow", "Load session", None))
        self.pushSaveSession.setText(_translate("MainWindow", "Save session", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Settings", None))
        self.label_3.setText(_translate("MainWindow", "Select Language", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "DB Glyph Properties", None))
        self.laDBGlyph.setText(_translate("MainWindow", "TextLabel", None))
        self.label_4.setText(_translate("MainWindow", "Select Glyph", None))
        self.pushUseDBGlyph.setText(_translate("MainWindow", "Use from db", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Chars DB", None))
        self.labVorher.setText(_translate("MainWindow", "TextLabel", None))
        self.label_5.setText(_translate("MainWindow", "Kernel Size", None))
        self.pushErode.setText(_translate("MainWindow", "Erode", None))
        self.pushDilate.setText(_translate("MainWindow", "Dilate", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), _translate("MainWindow", "Erode/Dilate", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_7), _translate("MainWindow", "Rotate", None))
        self.labNaher.setText(_translate("MainWindow", "TextLabel", None))
        self.label_6.setText(_translate("MainWindow", "Undo History", None))
        self.labHistory.setText(_translate("MainWindow", "TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Glyph", None))

def main():
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
   


if __name__ == '__main__':    
    main()
