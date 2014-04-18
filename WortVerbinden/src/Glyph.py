# -*- coding: UTF-8 -*- 
'''
Created on Mar 26, 2014

@author: phoenix
'''
import cv2
import numpy as np
class GlyphElement:
    '''
    classdocs
    '''
    


    def __init__(self, char,img_path):
        '''
        Constructor
        '''
        
        print 'Creating glyph for ',str(char).encode('utf-8'),'from',img_path
        self.Char=char;
        self.GraphemeImg=img_path
        self.Vorher=[]#This is an array that will store the original image
        self.Naher=[]#This is an array Man wollte dieses Bild verarbeiten
        #Das Bild will hier sein
        self.Width=0
        self.Height=0
        self.Top=0
        self.Low=0
        self.BaseLine=0
        self.SpecialChar=1
        
        
        
        
  


        
        #This is an undo history ....
        #It is a list of lists....
        #The first element is the original binarized image
        self.History=[]
        
     
        self.Vorher=cv2.imread(self.GraphemeImg,cv2.CV_LOAD_IMAGE_GRAYSCALE)
        
        ret2,self.Vorher = cv2.threshold(self.Vorher,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        
        self.Naher=self.Vorher
        
        
        
        
        self.DetectLines()
        
  
     
        
    def DetectLines(self):
        print 'Detecting lines'
        #get top low and baseline
        #get lowest black topmost black pixel

        self.Width,self.Height=self.Vorher.shape
        
        self.History.append(self.Naher)
        
        
        #check for special char
        
        self.Top=self.Height
       

        #------------------------Low and Top Line------------------------
        for y in range(0,self.Height):
            for x in range(0,self.Width):
                if self.Naher[x][y]==0 and y>self.Low:
                    self.Low=y
                if self.Naher[x][y]==0 and y<self.Top:
                    self.Top=y
                    
                    
        print ('Low Line for ',self.Char ,'is',self.Low)
        print ('TopLine for ',self.Char ,'is',self.Top)
        
        self.BaseLine=self.Low
        
        
             
      
