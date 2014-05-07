'''
Created on May 7, 2014

@author: phoenix
'''
#baselineis 69
import cv2
import numpy as np

#no grid just horizontal lines
#if whitespace more than a threshold 
#shift
qr=cv2.imread('/home/phoenix/Desktop/faq.png',cv2.CV_LOAD_IMAGE_GRAYSCALE)
qrcolor=cv2.imread('/home/phoenix/Desktop/faq.png',cv2.CV_LOAD_IMAGE_COLOR)

h,w=qr.shape
bline=69


 
#calc white space above the red line



Spaces=[]
for col in range(0,w):
      Scwarz=0
      
           
      for row in range(0,bline):
          
          if qr[row][col]==0:
              Scwarz=1
              # print 'A black pixel was found at',i,j
              
              
        
             
      if Scwarz==0:
          #print 'All white in col',col
          
          Spaces.append(1)
          #draw a blue line
          for i in range(0,bline):
              qrcolor[i][col][0]=0
              qrcolor[i][col][1]=0
              qrcolor[i][col][2]=255
      else:
          Spaces.append(0)



Mikos=[]
stopcol=0
start=0 # start col
m=0
print '-------------------------'
for s in Spaces:
    #print "s=",s
    start+=1
    if s==1:
        m+=1
    else:
        if m>12 and m<40:
            Mikos.append(start)
        
        m=0
        
for m in Mikos:
    print m
    stopcol=m
    


#shift all pixes from col 0 to m  and row o to bline
#by 12 
nospace= np.ones((h+20,w+20,1), np.uint8)
nospace.fill(255)

r=0
c=0
for row in range(0,bline):
    for col in range(0,stopcol):
        nospace[row][col+29]=qr[row][col] #widith of white space


for row in range(0,bline):
    for col in range(stopcol,w):
        nospace[row][col]=qr[row][col]

#descender
for row in reversed(range(bline,h)):
    for col in range(0,w):
        nospace[row][col]=qr[row][col]

 
cv2.imshow('red',qrcolor)
cv2.imshow('shift',nospace)


cv2.waitKey()
cv2.destroyAllWindows()   



     