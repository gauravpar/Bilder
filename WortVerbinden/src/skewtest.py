'''
Created on Apr 15, 2014

@author: phoenix
'''
import cv2,math
import numpy as np
from numpy import array # we ll use to calc linear regression equation
vorher=cv2.imread('/home/phoenix/Verbinden/testskew1.png',cv2.CV_LOAD_IMAGE_GRAYSCALE)
color=cv2.imread('/home/phoenix/Verbinden/testskew1.png',cv2.CV_LOAD_IMAGE_COLOR)


#Elina 's way
#the skew seems correct but the line detection does not



ret2,otzu = cv2.threshold(vorher,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

Height, Width=vorher.shape


#get the lowest black Elements
#Black pixel coordinates
x=[]
y=[]


for i in reversed(range(0,Height)):
    for j in range(0,Width):
        #get black pixels
        if otzu[i][j]==0:
            y.append(i)
            x.append(j)
            #color these pixels BLUE
            color[x][y][0]=255
            color[x][y][1]=0
            color[x][y][2]=0
            
            break
    else:
        continue


cv2.imshow('Colored dots',color)
print ('Black pixels are:')
for i in range(0,len(x)):
    print x[i],y[i]
    
     
a,b=np.polyfit(x, y, 1)

print 'a',a,'b',int(b) #b seems to be the upper main body line

rads=math.atan(a)
degs=(rads*180)/math.pi #it seems to WORK
print "angle in degrees",degs

cv2.imshow("Original",otzu)
#rotated Image



center=(Width/2,Height/2)



M=cv2.getRotationMatrix2D(center,degs,1.0) #the 1.0 has smth to do with scale

rot=cv2.warpAffine(otzu,M,(Width,Height))


cv2.imshow("Rotated",rot)
cv2.imwrite("/tmp/rotated.png",rot)

cv2.waitKey()
cv2.destroyAllWindows()
