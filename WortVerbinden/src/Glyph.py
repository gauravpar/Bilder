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
        
        print 'Creating glyph for ',str(char).encode('utf-8'),'from',img_path
        self.Char=char;
        self.GraphemeImg=img_path
         
        self.Vorher=[]#This is an array that will store the original image
        self.Naher=[]#This is an array Man wollte dieses Bild verarbeiten
        
        
        #Das Bild wird hier sein
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
        
        
        ret2,self.Vorher = cv2.threshold(self.Vorher,0,255,cv2.THRESH_OTSU)
        
        self.Naher=self.Vorher
        

        
        
        self.DetectLines()
        
  
     
        
    def DetectLines(self):
        print 'Detecting lines'
        #get top low and baseline
        #get lowest black topmost black pixel
        
        
        #SIGOYROTATA ETSI EINAI TO SWSTO

        self.Height,self.Width=self.Naher.shape
        
        self.History.append(self.Naher)
        
        
        #check for special char
        print 'Width',self.Width,'Height',self.Height
        self.Top=self.Height
       

        #------------------------Low and Top Line------------------------
        #Low Line lowest black pixel
        for i in range(0,self.Height):
        
            for j in range(0,self.Width):
                
                if self.Naher[i][j]==0 and i<self.Top:
                    self.Top=i
                if self.Naher[i][j]==0 and i>self.Low:
                    self.Low=i

           
        print ('Low Line for ',str(self.Char).encode('utf-8') ,'is',self.Low)
        print ('TopLine for ',str(self.Char).encode('utf-8') ,'is',self.Top)
        
        self.BaseLine=self.Low
        
        
             
      
