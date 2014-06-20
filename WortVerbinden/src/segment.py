# -*- coding: UTF-8 -*- 
'''
Created on Jun 19, 2014

@author: phoenix
'''
#character segmentation using vertical projection
import cv2,glob
import numpy as np
import matplotlib.pyplot as plt

VertY=[] #for each row
VertX=[] # count the  black pixels


gray=cv2.imread('/home/phoenix/Desktop/buchbilder/segment/s0.jpeg',cv2.CV_LOAD_IMAGE_GRAYSCALE)
ret2,test = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


Height,Width=test.shape #prota diavazei to ypsos kai meta to platos

print "Width",Width,"Height",Height



#Horizontal histogram


HorX=[] #for each column
HorY=[] # count the  black pixels

m=0 #for matplob figure
for col in range(0,Width):
    s=0

    for row in range(0,Height):
        
        if test[row][col]==0: #count the BLACK
            s+=1
    if s>m:
        m=s
        
    HorX.append(col)
    HorY.append(s)





zeroes=[] # We store the columns that have zero black pixels in HorY
#print horY Values
i=0
StartChar=0
EndChar=0
while i<len(HorY)-3:
    #print i,HorY[i],StartChar

        
    if HorY[i]!=0 and StartChar==0:
        StartChar=i-3
       
        
    if HorY[i]==0 and StartChar!=0:
        EndChar=i+3
        #print StartChar,EndChar
        char=[]
        char.append(StartChar)
        char.append(EndChar)
        zeroes.append(char)
       
        StartChar=0
        
        
    if HorY[i]==0:
        StartChar=0
    
    i+=1
    
  
  

#plot them
plt.plot(HorX,HorY)
plt.title("Horizontal Histogram")
plt.axis([0,Width,0,m])
plt.show()    




#cut the chars
print zeroes

#get the number of files in that folder
f=len(glob.glob('/home/phoenix/Desktop/buchbilder/chars/*'))
print 'files',f
f+=1

for charBBox in zeroes:
   
    #copy  pixels from row 0 to end
    #from col charBBox[0] to charBBox[1]
    #πρώτα μπαίνει το ύψος και μετά το πλάτος και μετά το πλήθος των καναλιών
    ch=np.ones((Height,charBBox[1]-charBBox[0]+1,1),np.uint8)
    ch.fill(255)


    h,w,d=ch.shape
    print 'ypsos',h,'platos',w

    print 'char from',charBBox[0],'to',charBBox[1]
    for row in range(0,Height):
        for col in range(0,charBBox[1]-charBBox[0]):
            print 'r',row,'c',col
            ch[row][col]=test[row][col-charBBox[0]]
            
    #show the char image
    cv2.imshow('char'+str(f),ch)
    cv2.imwrite('/home/phoenix/Desktop/buchbilder/chars/c'+str(f)+'.jpeg',ch,[cv2.IMWRITE_JPEG_QUALITY,95])
    f+=1
    cv2.waitKey()
    cv2.destroyAllWindows()

