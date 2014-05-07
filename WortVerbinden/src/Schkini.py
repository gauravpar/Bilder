import math,cv2,math
from PyQt4.QtGui import QGraphicsScene,QGraphicsSceneMouseEvent,QGraphicsRectItem
from PyQt4 import QtGui,QtCore
import numpy as np


#If the user is to click and select glyphs then an extended qgraphics scene class is needed
#if you can't do it it is already coded in C++

class Schkini(QGraphicsScene):
    Times=0;
    TmpFolder=''
    LowX=0
    LowY=0
    TopX=0
    TopY=0
    Mode=-1 #Mode 0 cuts glyphs Mode 1 area 's binarize sand corrects skew


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
            if self.Mode==0:
                Kuli.setColor(QtCore.Qt.magenta)
            if self.Mode==1:
                Kuli.setColor(QtCore.Qt.blue)

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
            print 'Saved to',self.TmpFolder+fname
            if self.Mode==0:
                copy.save(self.TmpFolder + fname +".jpg");
            if self.Mode==1:
                copy.save(self.TmpFolder + fname +".jpg");
                stravo=cv2.imread(self.TmpFolder + fname +".jpg",cv2.CV_LOAD_IMAGE_GRAYSCALE)
                stravo=self.CorrectSkew(stravo)
                cv2.imwrite(self.TmpFolder + fname +"rot.jpg",stravo)

                        
    def CorrectSkew(self,stravo):
        #Elina 's way
        #the skew seems correct but the line detection does not
        #stravo should be binarized
        Height,Width =stravo.shape
        print 'Width',Width,'Heigth',Height
        
        
        ret2,stravo= cv2.threshold(stravo,0,255,cv2.THRESH_OTSU)

        
        
        #get the lowest black Elements for each col
        #Black pixel coordinates
        x=[]
        y=[]
        
        
        for col in range(0,Width):
            
            for row in reversed(range(0,Height)):
                #get black pixels
                if stravo[row][col]==0:
                    y.append(row)
                    x.append(col)
                    break

        
        a,b=np.polyfit(x, y, 1)
        
        print 'a',a,'b',int(b) #b seems to be the upper main body line
        
        rads=math.atan(a)
        degs=rads*180/math.pi
        
        print "angle in degrees",degs
        
        
        
        #rotated Image
        
        
        
        center=(Height/2,Width/2)
        
        
        
        M=cv2.getRotationMatrix2D(center,degs,1.0) #the 1.0 has smth to do with scale
        
        isio=cv2.warpAffine(stravo,M,(Width,Height))
        return isio
              
       


        