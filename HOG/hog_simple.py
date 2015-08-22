# -*- coding: utf-8 -*-
from __future__ import division
import cv2,math
import numpy as np


'''
Local Gradient Histogram Features for Word Spotting in Unconstrained Handwritten Documents
J. Rodriguez F.Perronnin



Implemented Steps

Create a sliding window of width w and Height  h
Create 8 cells with equal dimensions in each window
For each cell get an 8 feature vector
For each pixel of the cell calculate Gx,Gy,Thetaxy
Add contributions to the cell vector accordingly
Concatenate the vector for each cell into a empty vector
This vector should have 4*4*8 dimensions
Normalize this vector according to the sum of all its elements NOT by its maximum
Concatenate the normalized vector to the image vector
'''

window_W = window_H = 20
window_Step = 20
T_BINS = 8
# eight bins
step = 2*math.pi/T_BINS

print 'step',step

#angle θ ranges from -pi to pi and so should the bins
ANGLE_BINS = [phi for phi in np.arange(-math.pi,math.pi+step,step)]
print 'bins:'
print ANGLE_BINS


def GetAngles(zell):

    H, W = zell.shape

    Gx = Gy = 0.0

    Cell_Feature = [0.0 for i in xrange(0, T_BINS)]
    #print len(Cell_Feature)
    for i in xrange(0, H):
        for j in xrange(0, W):

            # if off limits add the other edge pixels as if the image were continuous

            if i == H-1:
                Gx = -zell[0][j]
            elif i == 0:
                Gx = zell[H-1][j]
            else:
                Gx = zell[i+1][j] - zell[i-1][j]


            if j == W-1:
                Gy = -zell[i][j-1]
            elif j == 0:
                Gy = zell[i][j+1]
            else:
                Gy = zell[i][j+1]-zell[i][j-1]

            Mxy = math.sqrt(Gx**2 + Gy**2)
            Thetaxy = math.atan2(Gy,Gx)

            #print Gx,Gy,Mxy,Thetaxy
            #so we have contribution to
            #Thetaxy is denoted as θ in the paper
            #find the the closest bin to θ


            #Figure 3 page 4
            LeftBin = None #index of closest bin to Thetaxy that is denoted as a in the paper
            RightBin = None

            #Since we have 8 angles LeftBin and RightBin should be a multiple of PI/4


            for k in xrange(0, T_BINS):
                #find the largest k for which...

                if ANGLE_BINS[k] <= Thetaxy and ANGLE_BINS[k+1] >= Thetaxy:
                    LeftBin = k
                    RightBin = k+1
                    #print k

            #get the contributions

            # contribution of Mxy[1-a*T_Bins/(2pi) to bin a
            alpha = ANGLE_BINS[RightBin]-Thetaxy

            Cell_Feature[LeftBin] += Mxy*(1.0-(T_BINS*alpha)/(2*math.pi))

            # contribution of Mxy[T_Bins*a/(2pi) to bin 2*pi/T_Bins-a
            Cell_Feature[RightBin]+= Mxy*T_BINS*alpha/(2*math.pi)


    return Cell_Feature






def DecomposeToCells(winImg):
    """
    winImg Window image
    cellDim cell width,height
    in this exanmple a window is 20 by 20 so make cellDim = 5
    """
    cellDim = 5

    winH , winW = winImg.shape

    Window_Feats=[]

    for i in xrange(0, winH, cellDim):
        for j in xrange(0, winW, cellDim):
                #print 'cell starts at',i,j

                cell = winImg[i:i+cellDim, j:j+cellDim]

                Cell_Features = GetAngles(cell)




                for cf in Cell_Features:
                    Window_Feats.append(cf)


    #normalize according to sum
    s = sum( Window_Feats)


    for i in xrange(0,len(Window_Feats)):
        Window_Feats[i] /= s


    return Window_Feats




def main():


    img = cv2.imread('pennywise.png',cv2.CV_LOAD_IMAGE_GRAYSCALE)
    ret,img = cv2.threshold(img,0,255,cv2.THRESH_OTSU)

    vektor = [] # output
    H, W = img.shape

    print H, W

    # create Windows with step 5 no overlap
    for i in xrange(0,H , window_Step):
        for j in xrange(0,W , window_Step):
            #print 'Window starts at',i,j
            # numpy slice start:width
            win = img[i:i+window_Step, j:j+window_Step]
            win_vec = DecomposeToCells(win)
            for v in win_vec:
                vektor.append(v)


    vektor = np.array(vektor)
    vektor[np.isnan(vektor)] = 0
    print len(vektor)

if __name__=="__main__":
    main()


