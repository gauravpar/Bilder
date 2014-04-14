import math
from PyQt4.QtGui import QGraphicsScene,QGraphicsSceneMouseEvent,QGraphicsRectItem
from PyQt4 import QtGui,QtCore



#If the user is to click and select glyphs then an extended qgraphics scene class is needed
#if you can't do it it is already coded in C++

class Schkini(QGraphicsScene):
    Times=0;
    TmpFolder=''
    DocImagePath=''
    LowX=0
    LowY=0
    TopX=0
    TopY=0
    Epiloges=[] # Man findet hier die Grenze den Buchstabebilder
    BackFolder=''


    def __init__(self):
        QGraphicsScene.__init__(self)
        
        
        
    def mouseDoubleClickEvent(self, event):
        print 'Clicked on ',event.scenePos().x(),event.scenePos().y()
        #
        self.Times+=1
        if self.Times==1:
            self.LowX=event.scenePos().x()
            self.LowY=event.scenePos().y()
        elif self.Times==2:
            self.TopX=event.scenePos().x()
            self.TopY=event.scenePos().y()
            #draw a magenta rectangle around the selection
            
            Kuli=QtGui.QPen()
            
            Kuli.setWidth(2)
            Kuli.setColor(QtCore.Qt.magenta)
            
            epilogi=QtGui.QGraphicsRectItem()
            
            epilogi.setRect(QtCore.QRectF(self.LowX,self.LowY,abs(self.TopX-self.LowX),abs(self.TopY-self.LowY)))
            epilogi.setPen(Kuli)
            
            self.Times=0;
            
            self.addItem(epilogi)

            #save to disk
            
            
            
            BigPix=QtGui.QPixmap(self.DocImagePath)
            copy=QtGui.QPixmap()
            
            copy=BigPix.copy(self.LowX,self.LowY,abs(self.LowX-self.TopX),abs(self.LowY-self.TopY))
            fname=self.DocImagePath[self.DocImagePath.rindex("/")+1:]
            fname.replace(".", "_")
            fname+="_"+str(self.LowX) + "_"+str(self.LowY)
            fname+="_"+str(self.TopX) + "_"+str(self.TopY)
            print 'Saved to',fname
            copy.save(self.BackFolder+fname +".jpg");
            
                        
                
       


        