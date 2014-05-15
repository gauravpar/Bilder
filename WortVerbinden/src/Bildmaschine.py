# -*- coding: UTF-8 -*- 


import cv2,math
import numpy as np

class BildMaschine():
    #This is the main buchstabebilder engine
   
   

    def __init__(self, q,bildbook):
        self.Query=q
        self.BilderBuch=bildbook
        self.WorkFolder=''
        self.ShiftLeft=0
        self.ShiftDown=0

        
    def AnfangenWash(self):
        
        self.EstimateLetterSpace()
        print 'Synthesizing begins...'
        print 'String Query is',self.Query.replace('\n','')
        print 'Breaking query into chars:'
        #Image Query Dimensions
        QueryW=0
        QueryH=0
        
      
          
          
        #find the maximum X
        print 'Image Query Height',QueryH
        print 'Printing Glyphbook'
        #BE CAREFUL
        #THE IMAGE SIZE IN NOT THE CHARS IN THE GLYPH BOOK
        #It is the sum of all the chars of the query
        for c in self.Query:

            for gl in self.BilderBuch:
                if str(c) in gl.Char: #find the char in the glyphbook
       
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
            
    
        QueryH=2*QueryH + self.ShiftDown
                        
        print 'Let \'s go'
        print 'Image Query Height',QueryH
        print 'Image Query Width',QueryW
        
      
        ImgQuery=np.ones((QueryH,QueryW,1), np.uint8)
        ImgQuery.fill(255)   #A white image
     


      
        
        s_row=0+self.ShiftDown
        s_col=self.LetterSpace
        
        BaseLine=0 #the baseline is the line of the first char
        CharCount=0
        
        e=0
         
        for c in self.Query:
            print '------------------------------'
            print 'Next char to be app',c
            #find it in the glyphbook
            
           
            for gl in self.BilderBuch:
                if str(c) in gl.Char: #find the char in the glyphbook
                    print 'It will be loaded from',gl.GraphemeImg
                    #all in one line...
                    
                    
                    s_row=BaseLine- abs(gl.BaseLine-gl.Top)
                    
                    
                    
                    CharCount+=1
                    
                    
                    #The baseline of the first char is the baseline of the word
                    if CharCount==1:
                        BaseLine=self.ShiftDown+ (gl.BaseLine-gl.Top) #IT WORKS!!
                        s_row=self.ShiftDown
                        print 'Baseline is',BaseLine
                    
                   
                    
                    
                    
                    self.ConcatWash(s_col, s_row, ImgQuery, gl.Naher,gl.Top,gl.Low,gl.Left,gl.Right,e)
                    e=e+1
                    
                    
                    s_col+=+self.LetterSpace+gl.Right-gl.Left 
                    
            
        print 'Finished'
        cv2.imwrite(self.WorkFolder + str(self.Query).encode('utf-8')+'.jpg',ImgQuery,[cv2.IMWRITE_JPEG_QUALITY,95])
        cv2.imshow('Query',ImgQuery)
        cv2.waitKey()
        cv2.destroyAllWindows()
    
    
    def ConcatWash(self,StartCol,StartRow,qpic_arr,char_arr,top,low,left,right,e):
        #concatenate chars
        print 'Copying from col',left,'to',right
        print 'Copying from row',top,'to',low
        

        print 'Appending a glyph w to r',StartRow,'c',StartCol
        
        clean_char_arr=np.ones((low-top,right-left,1),np.uint8) #contains only the black pixels
        
        
        #snipets copies only black pixels
        for i in range(0,low-top):
            for  j in range(0,right-left):
                clean_char_arr[i][j]=char_arr[i+top][j+left]
        
        
        #cv2.imwrite("/tmp/pic" + str(e)+".png",clean_char_arr)
        
        
        
        #and pastes them to final image query
        for i in range(0, low-top):
            for j in range(0, right-left):
                qpic_arr[i+StartRow][j+StartCol]=clean_char_arr[i][j]
 
  
        #cv2.imwrite("/tmp/q" + str(e)+".png",qpic_arr)
  
    
  

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
        
    
  
    def EstimateLetterSpace(self):
        #Estimates in a very naïve way the space between chars
        #counts the white columns
        #for simplicity images are stored in /home/phoenix/Verbinden/whitespace

        self.LetterSpace=0
        amount=0
        for p in range(0,10):
            Spaces=[]
            print p
            test=cv2.imread(self.WorkFolder + "whitespace/space"+str(p)+".png",cv2.CV_LOAD_IMAGE_GRAYSCALE)

            test=self.CorrectSkew(test)
            
            
            Height,Width=test.shape
            #xekina apo aristera 
            #diavase olo to column 
            #an einai ola aspra simeiosate x
            
           
            for col in range(0,Width):
                Scwarz=0
                
                     
                for row in range(0,Height):
                    
                    if test[row][col]==0:
                        Scwarz=1
                        # print 'A black pixel was found at',i,j
                        
                        
                  
                       
                if Scwarz==0:
                    #print 'All white in col',col
                    
                    Spaces.append(1)
                    
                else:
                    Spaces.append(0)
            
            #count the thickness of the red lines that is count the length of ones
            Mikos=[]
            m=0
            print '-------------------------'
            for s in Spaces:
                #print "s=",s
                if s==1:
                    m+=1
                else:
                    if m>0:
                        Mikos.append(m)
                    m=0
                    
            amount+=len(Mikos)
            for m in Mikos:
                print m
                self.LetterSpace+=m
            #find m average
            
        print 'Letter space is ',self.LetterSpace    
        self.LetterSpace=int(self.LetterSpace/amount)
       
        print 'amount is ',amount
        print 'Letter space is ',self.LetterSpace
            



    def ConcatSamos(self,StartCol,StartRow,qpic_arr,char_arr,left,right,ypsos):
        #concatenate chars
        print 'Copying from col',left,'to',right

        print 'Appending a glyph w to r',StartRow,'c',StartCol
        
        clean_char_arr=np.ones((ypsos,right-left,1),np.uint8) #contains only the black pixels
        
        #and not the white space left and right
        for i in range(0,ypsos):
            for  j in range(0,right-left):
                clean_char_arr[i][j]=char_arr[i][j+left]
        
        
        for i in range(0, ypsos):
            for j in range(0, right-left):
                qpic_arr[i+StartRow][j+StartCol]=clean_char_arr[i][j]
 
    
           
    def AnfangenSamos(self):
        
        self.EstimateLetterSpace()
        print 'Synthesizing begins...'
        print 'String Query is',self.Query.replace('\n','')
        print 'Breaking query into chars:'
        #Image Query Dimensions
        QueryW=0
        QueryH=0
        
          
          
        #find the maximum X
        print 'Image Query Height',QueryH
        print 'Printing Glyphbook'
        #BE CAREFUL
        #THE IMAGE SIZE IN NOT THE CHARS IN THE GLYPH BOOK
        #It is the sum of all the chars of the query
        for c in self.Query:

            for gl in self.BilderBuch:
                if str(c) in gl.Char: #find the char in the glyphbook
       
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
            
    
        QueryH=2*QueryH + self.ShiftDown
                
        print 'Let s go'
        print 'Image Query Height',QueryH
        print 'Image Query Width',QueryW
        
      
        ImgQuery=np.ones((QueryH,QueryW,1), np.uint8)
        ImgQuery.fill(255)   #A white image
     


      
        
        s_row=0+self.ShiftDown
        s_col=self.LetterSpace
        
        BaseLine=0 #the baseline is the line of the first char
        CharCount=0
        
        e=0
         
        for c in self.Query:
            print '------------------------------'
            print 'Next char to be app',c
            #find it in the glyphbook
            
           
            for gl in self.BilderBuch:
                if str(c) in gl.Char: #find the char in the glyphbook
                    print 'It will be loaded from',gl.GraphemeImg
                    #all in one line...
                    
                    
                    s_row=BaseLine- abs(gl.BaseLine-gl.Top)                    
                    
                    
                    CharCount+=1
                    
                    
                    #The baseline of the first char is the baseline of the word
                    if CharCount==1:
                        BaseLine=self.ShiftLeft+ (gl.BaseLine-gl.Top) #IT WORKS!!
                        s_row=self.ShiftDown
                        print 'Baseline is',BaseLine
                    
                    
                    
                    
                    self.ConcatSamos(s_col, s_row, ImgQuery, gl.Naher,gl.Left,gl.Right,gl.Height)
                    e=e+1
                    
                    
                    s_col+=+self.LetterSpace+gl.Right-gl.Left 
                    
            
        print 'Finished'
        cv2.imwrite(self.WorkFolder + 'query.png',ImgQuery)
        cv2.imshow('Query',ImgQuery)
        cv2.waitKey()
        cv2.destroyAllWindows()
    
          
   
        
    def CorrectSkew(self,stravo):
        #Elina 's way
        #the skew seems correct but the line detection does not
        #stravo should be binarized
        Height,Width =stravo.shape
        print 'Width',Width,'Heigth',Height
        
        
        
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
    
    
         
    
    
    
  
  
    def PostProcess(self):
        pass