# -*- coding: utf-8 -*-

#select any of the installed system fonts
import sys,cv2,math
from PyQt4 import QtCore, QtGui
from Vorbereiten import Vorbereiten
from PyQt4.Qt import QFontDatabase, QPixmap, QApplication, QCursor
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QApplication, QCursor
import numpy as np

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
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(399, 653)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(40, 175, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 175, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 175, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 175, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(144, 141, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 147, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(70, 60, 291, 381))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.listFonts = QtGui.QListWidget(self.groupBox)
        self.listFonts.setGeometry(QtCore.QRect(20, 30, 251, 331))
        self.listFonts.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listFonts.setObjectName(_fromUtf8("listFonts"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 460, 91, 61))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineTempFolder = QtGui.QLineEdit(self.centralwidget)
        self.lineTempFolder.setGeometry(QtCore.QRect(120, 480, 271, 21))
        self.lineTempFolder.setObjectName(_fromUtf8("lineTempFolder"))
        self.pushQuery = QtGui.QPushButton(self.centralwidget)
        self.pushQuery.setGeometry(QtCore.QRect(150, 570, 99, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushQuery.setFont(font)
        self.pushQuery.setObjectName(_fromUtf8("pushQuery"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 51))
        self.label.setObjectName(_fromUtf8("label"))
        self.labPaint = QtGui.QLabel(self.centralwidget)
        self.labPaint.setGeometry(QtCore.QRect(20, 20, 591, 471))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.labPaint.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.labPaint.setFont(font)
        self.labPaint.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.labPaint.setMargin(55)
        self.labPaint.setObjectName(_fromUtf8("labPaint"))
        self.lineWordList = QtGui.QLineEdit(self.centralwidget)
        self.lineWordList.setGeometry(QtCore.QRect(90, 20, 271, 21))
        self.lineWordList.setObjectName(_fromUtf8("lineWordList"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 520, 91, 61))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineFolder = QtGui.QLineEdit(self.centralwidget)
        self.lineFolder.setGeometry(QtCore.QRect(120, 540, 271, 21))
        self.lineFolder.setObjectName(_fromUtf8("lineFolder"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        #my code
        self.labPaint.setVisible(False)
        self.lineWordList.setText('/home/phoenix/Desktop/handcraft/lexeis.txt')
        self.lineFolder.setText("/home/phoenix/Desktop/noscale/")
        self.lineTempFolder.setText('/tmp/')
        #get installed fonts
        fontdb=QFontDatabase()
        for font in fontdb.families():
            f=QtGui.QFont(font)
            f.setPointSize(12)
            f.setPixelSize(12)
            it=QtGui.QListWidgetItem()
            it.setFont(f)
            it.setText(font)
            self.listFonts.addItem(it)
            
        
        
        #SLOTS
        QtCore.QObject.connect(self.pushQuery,QtCore.SIGNAL('clicked()'),self.GenerateSynthetic)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Query Synthesis", None))
        self.groupBox.setTitle(_translate("MainWindow", "Select fonts", None))
        self.label_2.setText(_translate("MainWindow", "Temp", None))
        self.pushQuery.setText(_translate("MainWindow", "GO!", None))
        self.label.setText(_translate("MainWindow", "Query", None))
        self.labPaint.setText(_translate("MainWindow", "TextLabel", None))
        self.label_3.setText(_translate("MainWindow", "Output folder", None))   
      
        
        
        
    def GenerateSynthetic(self):
        
        #calc shear angles here 
        shear_angles=[]
        #DONT calculate histogram at the original image...
        for a in np.arange(-math.pi/2.8,math.pi/2.8,math.pi/95.0): #this should be be in radians!!! 3 degrees loop
            shear_angles.append(a)
            
            
        self.pushQuery.setVisible(False)
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        
        VB=Vorbereiten()
        #generate queries in the self.Folder
        #read the self.WordList file
        
        SelectedFonts=[]
        WordList=[]
        item=self.listFonts.selectedItems()

        for l_item in item:
            SelectedFonts.append(str(l_item.text()).encode('utf-8'))
            
        
            
        print SelectedFonts
        
        #read word list file
        
        with open(self.lineWordList.text()) as WF:
            for line in WF:
                WordList.append(line.replace('\n',''))
     
        WF.close()
        print WordList
        self.labPaint.setVisible(True)
         
         
        TotalImages=len(WordList)*len(SelectedFonts)       
        #for each font
            #for each word
        for f in SelectedFonts:
            
            for w in WordList:
                grammatoseira=QtGui.QFont()
                grammatoseira.setFamily(f)
                grammatoseira.setPixelSize(15)
                grammatoseira.setPointSize(15)
                grammatoseira.setLetterSpacing(QtGui.QFont.AbsoluteSpacing,2)
                grammatoseira.setStyleStrategy(QtGui.QFont.NoAntialias)
                self.labPaint.setText(w)
                self.labPaint.setFont(grammatoseira)
    
                QApplication.processEvents()
     
                #save the image to a tmp folder
                pixie=QPixmap()
        
                pixie = QPixmap.grabWidget(self.labPaint, self.labPaint.rect())
     
                #transmute QtString to str
                filename=self.lineTempFolder.text() +'synth_'+str(f).encode('utf-8')+'_'+ w +'.png'
                pixie.save(filename,'PNG')
        
                print 'generated',w,'using',f,'saved at',filename
                #deslant  
                #VB.deslant(str(filename), str(filename),shear_angles)
                print 'deslanting...'
                VB.Vinciarelli(str(filename), str(filename),shear_angles)
                print 'corrected slant for',filename
                        
        
                #crop 
                print 'cropping...'

                VB.Crop(str(filename), str(filename))
                print 'cropped',filename

            
        
                #scale on the fly
                print 'scaling...'

                arr=VB.Scale(str(filename), 0)
                
                print 'scaled'
                #save on the new folder
                cv2.imwrite(str(self.lineFolder.text()) + 'synth_' + str(f).encode('utf-8')+'_'+  str(w)+'.png',arr,[cv2.IMWRITE_PNG_COMPRESSION,95])
                print 'saved'
                
                TotalImages-=1
                print 'remaining to be synthesized',TotalImages
        
        print 'End of generation and normalizing'
        #Extract features
        #featEX=FeatExtractor(str(self.lineFolder.text()),'/home/phoenix/Desktop/handcraft/synth_feats.txt','/home/phoenix/Desktop/handcraft/synth_lexeis.txt')
        print 'Extracted features'

        
        
        #restore cursor
        QApplication.restoreOverrideCursor()
        
        #show results
        print 'Done'
        
        
     
        

def main():
    reload(sys)
    sys.setdefaultencoding('UTF8')
    app=QtGui.QApplication(sys.argv)
    MainWindow=QtGui.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    

if __name__=='__main__':
    main()
    
    

