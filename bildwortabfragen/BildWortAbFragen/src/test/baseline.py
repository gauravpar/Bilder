
#baseline estimation for handwritten get horizontal profile
#find maxima....
import cv2
import numpy as np
import matplotlib.pyplot as plt
from _sqlite3 import Row


im=cv2.imread('/home/phoenix/Markov/Test/test3.jpeg',cv2.CV_LOAD_IMAGE_GRAYSCALE)
imcol=cv2.imread('/home/phoenix/Markov/Test/test3.jpeg',cv2.CV_LOAD_IMAGE_COLOR)

ret,test=cv2.threshold(im,0,255,cv2.THRESH_OTSU)

Height,Width=im.shape



HorX=[] #black pixels
HorY=[] # rows
#Horizontal histogram

bline=0
max=0 #for matplob figure
for row in xrange(0,Height):
    sum=0

    for col in xrange(0,Width):
        
        if test[row][col]==0: #count the BLACK
            sum+=1
            
    if sum>max:
        max=sum
        bline=row
        
    HorY.append(row)
    HorX.append(sum)


print 'baseline is at',bline

for j in xrange(0,Width):
    imcol[bline][j][0]=255
    imcol[bline][j][1]=0
    imcol[bline][j][2]=0

cv2.imshow('base line',imcol)
cv2.waitKey()
cv2.destroyAllWindows()

#plot them
plt.plot(HorX,HorY)
plt.title("Horizontal Histogram")
plt.axis([0,max+20,0,Height])
plt.show()
