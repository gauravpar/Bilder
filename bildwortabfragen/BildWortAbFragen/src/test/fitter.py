
#take a part of a character
#find a polynomial approximation....
import cv2
import matplotlib.pyplot as plt
from skimage.morphology import skeletonize
import numpy as np
#erode erode skeletonize....

image=cv2.imread('/home/phoenix/Markov/Test/F.jpeg',cv2.CV_LOAD_IMAGE_GRAYSCALE)
ret,im_bin=cv2.threshold(image,0,255,cv2.THRESH_OTSU)

#skeleton = skeletonize(image)
cv2.imshow('test',im_bin)
#cv2.imshow('test',skeleton)
cv2.waitKey()
cv2.destroyAllWindows()

Height,Width=im_bin.shape
print 'Platos',Width,'Ypsos',Height
Xs=[]
Ys=[]


#dont forget origin is at top left
for row in range(0,Height):
    for col in xrange(0,Width):
        if im_bin[row][col]==0: #if the pixel is black append the coordinates
            Ys.append(float(Height-row))
            Xs.append(float(col))
            
print Xs
print Ys

#plot the actual points!!!

#plt.plot(Xs, Ys, 'ro')
#plt.show()


#polyfit
coeffs=np.polyfit(np.array(Xs), np.array(Ys),3) #approximated coefficients
print coeffs

#plot 
my_poly=np.poly1d(coeffs)

Xs_bar=[]
Ys_bar=[]

for x in xrange(0,100):
    Xs_bar.append(x)
    Ys_bar.append(my_poly(x))
    
    
 
plt.plot(Xs_bar, Ys_bar, 'ro')
plt.show()
       