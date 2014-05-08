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

h,w=qr.shape
bline=68


 
#calc white space above the red line

#many stop cols #last element of stopfiles is the width
stopstiles=[139,260,w] 
noblank=[24,24,0]
charwidth=[48,48,0]


#stopcol=1
#while stopcol>0:
#    stopcol=int(raw_input("enter stop col"))
#    nowhite=int(raw_input("no white space"))
#    stopstiles.append(stopcol)
#    noblank.append(nowhite)


#shift all pixes from col 0 to m  and row o to bline
#by 12 
nospace= np.ones((h+20,w+20,1), np.uint8)
nospace.fill(255)

r=0
c=0


picid=0

#copy all the pixels up to the first stop col
for row in range(0,bline):
    for col in range(0,stopstiles[0]):
        nospace[row][col]=qr[row][col]

cv2.imshow('shift '+ str(picid),nospace)

picid+=1

for q in range(0,1):
    print 'q is ',q
    #progressive shifting
    #shift all pixel right from  stopcol+noblack  to stopcol[1] to the left by no blank
    
    #copy main body!!!
    for row in range(0,bline):
        for col in range(stopstiles[q],stopstiles[q+1]):
            nospace[row][col]=qr[row][col+noblank[q]]
    
    cv2.imshow('shift ' + str(picid),nospace)
    
    #copy descender!!!
    for row in reversed(range(bline,h)):
        for col in range(stopstiles[q],stopstiles[q]+charwidth[q]):
            nospace[row][col-noblank[q]]=qr[row][col]
    
    
    
    cv2.imshow('shift ' + str(picid),nospace)

    picid+=1
    
    
cv2.imshow('original',qr)
cv2.imshow('final',nospace)


cv2.waitKey()
cv2.destroyAllWindows()   



     