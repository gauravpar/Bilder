# -*- coding: UTF-8 -*- 


import cv2
import numpy as np

class BildMaschine():
    #This is the main buchstabebilder engine
   
   

    def __init__(self, q,bildbook):
        self.Query=q
        self.BilderBuch=bildbook
        self.LetterSpace=21

        
    def Anfangen(self):
        
        
        print 'Synthesizing begins...'
        print 'String Query is',self.Query.replace('\n','')
        print 'Breaking query into chars:'
        #Image Query Dimensions
        QueryW=0
        QueryH=0
        #find the maximum X
        print 'Image Query Height',QueryH
        print 'Printing Glyphbook'
        for gl in self.BilderBuch:
            print '----------------------------'
            print gl.Char
            print 'Width',gl.Width
            print 'Height',gl.Height
            print 'Left Line',gl.Left
            print 'Right Line',gl.Right
            print 'Top Line',gl.Top
            print 'Low Line',gl.Low
            print 'Base line',gl.BaseLine
            QueryW+=gl.Width+self.LetterSpace #!!!!!
            if gl.Height>QueryH:
                QueryH=gl.Height
                
    
        QueryH*=2
                
        print 'Let \'s go'
        print 'Image Query Height',QueryH
        print 'Image Query Width',QueryW
        
      
        ImgQuery=np.ones((QueryH,QueryW,1), np.uint8)
        ImgQuery.fill(255)   #A white image
     


        Shift=2
        
        s_row=0+Shift
        s_col=0
        
        BaseLine=0 #the baseline is the line of the first char
        CharCount=0
        
        for c in self.Query:
            print '------------------------------'
            print 'Next char to be app',c
            #find it in the glyphbook
            for gl in self.BilderBuch:
                if str(c) in gl.Char: #find the char in the glyphbook
                    print 'It will be loaded from',gl.GraphemeImg
                    #all in one line...
                    s_row=abs(gl.BaseLine-BaseLine)+Shift
                   
                    
                    CharCount+=1
                    
                    if CharCount==1:
                        BaseLine=gl.BaseLine
                        s_row=Shift
                    
                    self.Concat(s_col, s_row, ImgQuery, gl.Naher,gl.Left,gl.Right,gl.Height)
                    
                    s_col+=+self.LetterSpace+gl.Right
                    
            
        print 'Finished'
        cv2.imwrite('/tmp/query.png',ImgQuery)
    
    
    def Concat(self,StartCol,StartRow,qpic_arr,char_arr,links,rechts,ypsos):
        #concatenate chars
        print 'Appending a glyph w to r',StartRow,'c',StartCol
        for i in range(0, ypsos):
            for j in range(links, rechts):
                qpic_arr[i+StartRow][j+StartCol]=char_arr[i][j]
 
            
   

    def Erode(self,img,kernel):
        return cv2.erode(img,kernel,iterations=1)
    
    
    def Dilate(self,img,kernel):
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
        
    
  
    #def EstimateLetterSpace(self):
    #    #Estimates in a very naïve way the space between chars
        
    #def EstimateWordSpace(self):
    #    #Estimates in a very naïve way the space between words