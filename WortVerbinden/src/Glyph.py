# -*- coding: UTF-8 -*- 

import cv2
class GlyphElement:



    def __init__(self, char,img_path):

        
        print 'Creating glyph for ',str(char).encode('utf-8'),'from',img_path
        self.Char=char
        self.GraphemeImg=img_path
         
        self.Vorher=[] #This is an array that will store the original image
        self.Naher=[]  #This is an array Man moechte dieses Bild verarbeiten
        
        #Glyph properties
        self.Width=0
        self.Height=0
        self.Top=0
        self.Low=0
        self.BaseLine=0
        self.SpecialChar=1
        self.TopBaseLine=0 # some chars may not have the same scale
        self.Left=0 #Poy xenika kai poy teleinwnei o char 
        self.Right=0
        
  


        
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
        for i in xrange(0,self.Height):
        
            for j in xrange(0,self.Width):
                
                if self.Naher[i][j]==0 and i<self.Top:
                    self.Top=i
                if self.Naher[i][j]==0 and i>self.Low:
                    self.Low=i

        self.BaseLine=self.Low 
        
#         
        #Detect Vertical Lines
        

        HorX=[] #for each column
        HorY=[] # count the  black pixels
        
        
        for col in xrange(0,self.Width):
            sum=0
        
            for row in xrange(0,self.Height):
                
                if self.Naher[row][col]==0: #count the BLACK
                    sum+=1
         
            HorX.append(col)
            HorY.append(sum)

        
        #now the left is the first non zero sum from top
        #and right the first non zero from bottom
        q=0
        while (q<len(HorY)):
            if HorY[q]>0:
                self.Left=q
                break
            q+=1
            
            
            
        q=len(HorY)
        while (q>0):
            q-=1
            if HorY[q]>0:
                self.Right=q
                break
            q-=1
            
        
        
        
        

        #Manual baseline fix for special characters

        if 'ξ' in self.Char:
            print 'Special Char'  
            self.BaseLine=self.Low-12
        
        if 'φ' in self.Char:
            print 'Special Char'  
            self.BaseLine=self.Low-10
        if 'χ' in self.Char:
            print 'Special Char'  
            self.BaseLine=self.Low-12
        if 'ψ' in self.Char:
            print 'Special Char'  
            self.BaseLine=self.Low-10
        if 'γ' in self.Char:
            print 'Special Char'  
            self.BaseLine=self.Low-12

        if 'η' in self.Char:
            print 'Special Char'  
            self.BaseLine=self.Low-9
            
        if 'ή' in self.Char:
            print 'Special Char'  
            self.BaseLine=self.Low-9
          
          
        if 'ἡ' in self.Char:
            print 'Special Char'  
            self.BaseLine=self.Low-10
                
        if 'ῆ' in self.Char:
            print 'Special Char'  
            self.BaseLine=self.Low-11
  
        if 'ζ' in self.Char:
            print 'Special Char'  
            self.BaseLine=self.Low-10
        if 'ς' in self.Char:
            print 'Special Char'  
            self.BaseLine=self.Low-4
        
        if 'ρ' in self.Char:
            print 'Special Char'  
            self.BaseLine=self.Low-9
        if 'μ' in self.Char:
            print 'Special Char'  
            self.BaseLine=self.Low-11
            
          
    
    
    
        
        
        print ('Left Line for ',str(self.Char).encode('utf-8') ,'is',self.Left)
        print ('Right Line for ',str(self.Char).encode('utf-8') ,'is',self.Right)
         
        print ('Low Line for ',str(self.Char).encode('utf-8') ,'is',self.Low)
        print ('BaseLine for ',str(self.Char).encode('utf-8') ,'is',self.BaseLine)
        print ('TopLine for ',str(self.Char).encode('utf-8') ,'is',self.Top)
        
        #errors may occur
        self.Left-=1
        self.Right+=1
        self.Top-=1
        self.Low+=1
        self.BaseLine+=1
        
        
        
             
      
