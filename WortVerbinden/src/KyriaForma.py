#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import sys
from PyQt4 import QtCore, QtGui
from Glyph import GlyphElement
from PyQt4.QtSql import *
from PyQt4.Qt import QListWidgetItem

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
    GlyphBook=[] # Hier  stehen die Buchstaben und ihre Bilder 
    Norm_Methods=['Scaling','Thickness','Slant','Skew','Whitespace','Baseline','Word Height']
    ComboList=[]
    Glyph_Chars=[]
    Sprache=''
    vasi = QSqlDatabase.addDatabase("QMYSQL");
    
    
        
        
    def UpdateTable(self):
        #print 'Updating List widget'
        #clear table and create as many columns as the distinct characters
        
        print 'Distinct characters in query'
        
        temp=QtCore.QString().fromUtf8(self.textQuery.toPlainText())
        self.Glyph_Chars=[]
        self.GlyphBook=[]
        for char in temp:
            #skip empty space and enter aka escape char
            if "\n" not in char and " " not in char and char not in self.Glyph_Chars: # to glyph car periexei tous diakritous xaraktires
                
                self.Glyph_Chars.append(char)
                gl=GlyphElement(char,'')
                self.GlyphBook.append(gl)
                print char
        #populate listwidget GlypWidget
        self.glyphWidget.clear();
        #Color should be red that mean's no grapheme has been choosed
        for char in self.Glyph_Chars:
            charListItem=QtGui.QListWidgetItem()
            charListItem.setText(char)
            charListItem.setTextColor(QtCore.Qt.red)
            self.glyphWidget.addItem(charListItem)
    
        
       
    def Go(self):
        print 'Order of normalization'
        for c in self.ComboList:
            print c.currentText()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(796, 676)
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
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 781, 161))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.textQuery = QtGui.QTextEdit(self.groupBox)
        self.textQuery.setGeometry(QtCore.QRect(10, 20, 761, 131))
        self.textQuery.setToolTip(_fromUtf8(""))
        self.textQuery.setWhatsThis(_fromUtf8(""))
        self.textQuery.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textQuery.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textQuery.setObjectName(_fromUtf8("textQuery"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 180, 221, 481))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.labGlyhPreview = QtGui.QLabel(self.groupBox_2)
        self.labGlyhPreview.setGeometry(QtCore.QRect(60, 380, 91, 101))
        self.labGlyhPreview.setObjectName(_fromUtf8("labGlyhPreview"))
        self.glyphWidget = QtGui.QListWidget(self.groupBox_2)
        self.glyphWidget.setGeometry(QtCore.QRect(10, 30, 201, 341))
        self.glyphWidget.setObjectName(_fromUtf8("glyphWidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(250, 180, 541, 491))
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
        self.labFinal.setGeometry(QtCore.QRect(10, 10, 501, 151))
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
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 20, 171, 371))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.charWidget = QtGui.QListWidget(self.tab)
        self.charWidget.setGeometry(QtCore.QRect(20, 20, 131, 431))
        self.charWidget.setObjectName(_fromUtf8("charWidget"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.graphicsView = QtGui.QGraphicsView(self.tab_3)
        self.graphicsView.setGeometry(QtCore.QRect(20, 110, 501, 192))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.label_2 = QtGui.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 71, 41))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.comboBox = QtGui.QComboBox(self.tab_3)
        self.comboBox.setGeometry(QtCore.QRect(110, 40, 251, 23))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(668, 162, 111, 31))
        self.comboSprache = QtGui.QComboBox(self.tab)
        self.comboSprache.setGeometry(QtCore.QRect(310, 50, 161, 23))
        self.comboSprache.setObjectName(_fromUtf8("comboSprache"))
        self.comboSprache.addItem('Greek')
        self.comboSprache.addItem('English')
        self.laDBGlyph = QtGui.QLabel(self.tab)
        self.laDBGlyph.setGeometry(QtCore.QRect(280, 120, 91, 91))
        self.laDBGlyph.setObjectName(_fromUtf8("laDBGlyph"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(190, 40, 111, 41))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # My methods-----------------------------------------
        self.lineTemp.setText('/tmp/')
        #combo box with all possible normalization methods
        
        for i in range(0,self.Norm_Methods.__len__()):
            combo=QtGui.QComboBox()
            for n in self.Norm_Methods:
                combo.addItem(n)
                combo.setCurrentIndex(i)
            self.ComboList.append(combo)
            self.verticalLayout.addWidget(combo)
        self.GetGlyphsFromDB()
        #slots
        QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL('clicked()'),self.Go)
        QtCore.QObject.connect(self.textQuery,QtCore.SIGNAL('textChanged()'),self.UpdateTable)
        self.charWidget.itemClicked.connect(self.ShowDBGlyph)
        self.comboSprache.currentIndexChanged.connect(self.LangChoice)

    def LangChoice(self,index):
        self.Sprache=self.comboSprache.currentText()
        print 'Language set to ' + self.Sprache
               
    def ShowDBGlyph(self,item):
        print 'Fetching glyph for ' + item.text()
        pixie=QtGui.QPixmap()
        self.vasi.open()
        query=QSqlQuery()
        query.prepare("Select Pic From Glyphs Where CharID IN (SELECT CharID FROM `Chars` WHERE `Text` LIKE :char)")
        query.bindValue(":char", item.text())
        query.exec_()
        while (query.next()):
            pixie.loadFromData(query.value(0).toByteArray(),"PNG")
        self.laDBGlyph.setPixmap(pixie)
        
        
        
    def GetGlyphsFromDB(self):
        #fetch greek chars from mysql
        try:
            print 'Reading chars from DB'
            self.vasi.setHostName("localhost")
            self.vasi.setDatabaseName("Kathareyousan")
            self.vasi.setUserName("reichstag")
            self.vasi.setPassword("reichstag")
            self.vasi.open()
            query=QSqlQuery(self.vasi)
            query.exec_("Select C.Text From Chars C,Glyphs G Where C.LangID=1 AND C.CharID=G.CharID")
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
            
        
        

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Word Synthesis", None))
        self.label_3.setText(_translate("MainWindow", "Select Language", None))
        self.groupBox.setTitle(_translate("MainWindow", "String Query", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Glyphs", None))
        self.labGlyhPreview.setText(_translate("MainWindow", "TextLabel", None))
        self.labFinal.setText(_translate("MainWindow", "TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabResults), _translate("MainWindow", "Results", None))
        self.label.setText(_translate("MainWindow", "Temp Folder", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Order of Normalization", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Greek chars DB", None))
        self.label_2.setText(_translate("MainWindow", "Font", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Washington", None))
        self.pushButton.setText(_translate("MainWindow", "GO", None))

def main():
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
   
    MainWindow.show()
    sys.exit(app.exec_())
   


if __name__ == '__main__':    
    main()
