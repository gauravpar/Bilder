# -*- coding: UTF-8 -*- 
'''
Created on Mar 26, 2014

@author: phoenix
'''
import cv2
class GlyphElement:
    '''
    classdocs
    '''
    


    def __init__(self, char,img_path):
        '''
        Constructor
        '''
        self.Char=char;
        self.GraphemeImg=img_path
        
        self.Width=0
        self.Height=0
        self.Top=0
        self.Low=0
        self.BaseLine=0
        self.SpecialChar=1
        self.DetectLines()
        
        
    #Bilderverarbeitung
    def DetectLines(self):
        #get top low and baseline
        #get lowest black topmost black pixel
        tmp=cv2.imread(self.GraphemeImg,cv2.CV_LOAD_IMAGE_GRAYSCALE)
        ret2,self.Glyph = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        self.Width,self.Height=self.Glyph.shape
        
        self.Top=self.Height
       

        #------------------------Low and Top Line------------------------
        for y in range(0,self.Height):
            for x in range(0,self.Width):
                if self.Glyph[x][y]==0 and y>self.Low:
                    self.Low=y
                if self.Glyph[x][y]==0 and y<self.Top:
                    self.Top=y
                    
                    
        print ('Low Line for ',self.Char ,'is',self.Low)
        print ('TopLine for ',self.Char ,'is',self.Top)
        
        self.BaseLine=self.Low
        
        
             
      
