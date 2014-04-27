'''
Created on Apr 15, 2014

@author: phoenix
'''
import cv2,math
import numpy as np

imagepath=raw_input("give image path")
vorher=cv2.imread(imagepath,cv2.CV_LOAD_IMAGE_GRAYSCALE)
xroma=cv2.imread(imagepath,cv2.CV_LOAD_IMAGE_COLOR)



#Elina 's way
#the skew seems correct but the line detection does not



ret2,otzu = cv2.threshold(vorher,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

Height,Width =vorher.shape
print 'Width',Width,'Heigth',Height



#get the lowest black Elements for each col
#Black pixel coordinates
x=[]
y=[]


for col in range(0,Width):
    
    for row in reversed(range(0,Height)):
        #get black pixels
        if otzu[row][col]==0:
            y.append(row)
            x.append(col)
            #color these pixels red
            xroma[row][col][0]=0
            xroma[row][col][1]=0
            xroma[row][col][2]=255
            break


cv2.imshow('Colored dots',xroma)
print ('Black pixels are:')
for i in range(0,len(x)):
    print 'row',x[i],'col',y[i]
    

a,b=np.polyfit(x, y, 1)

print 'a',a,'b',int(b) #b seems to be the upper main body line

rads=math.atan(a)
degs=rads*180/math.pi

print "angle in degrees",degs



#rotated Image



center=(Height/2,Width/2)



M=cv2.getRotationMatrix2D(center,degs,1.0) #the 1.0 has smth to do with scale

rot=cv2.warpAffine(otzu,M,(Width,Height))


cv2.imshow("Rotated",rot)
cv2.imwrite("/tmp/dots.png",xroma)

cv2.imwrite("/tmp/rotated.png",rot)

cv2.waitKey()
cv2.destroyAllWindows()
