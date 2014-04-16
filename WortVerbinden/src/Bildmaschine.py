# -*- coding: UTF-8 -*- 


import cv2
import numpy as np

class BildMaschine():
    #This is the main buchstabebilder engine
   
   

    def __init__(self, q,bildbook):
        self.Query=q
        self.BilderBuch=bildbook


        
    def Anfangen(self):
        print 'Synthesizing begins...'
        print 'String is',self.Query
        print 'Breaking query into chars:'
        for c in self.Query:
            print c
 
         
    def Erode(self,img,kernelSize):
        kernel = np.ones((kernelSize,kernelSize),np.uint8)
        return cv2.erode(img,kernel,iterations=1)
    
    
    def Dilate(self,img,kernelSize):
        kernel = np.ones((kernelSize,kernelSize),np.uint8)
        return cv2.dilate(img,kernel,iterations=1)
    
    def Otsu(self,img):
        ret2,otsu = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)  
        return otsu
    
    def Rotate(self,pic_arr,value):
        #if value is negative counter clockwise
        (h,w)=pic_arr.shape[:2]
        center=(w/2,h/2)
        M=cv2.getRotationMatrix2D(center,value,1.0)
        return cv2.warpAffine(pic_arr,M,(w,h))   
        
    
    
        
    #def Concat(self):
    #    #concatenate chars
        
    #def EstimateLetterSpace(self):
    #    #Estimates in a very naïve way the space between chars
        
    #def EstimateWordSpace(self):
    #    #Estimates in a very naïve way the space between words