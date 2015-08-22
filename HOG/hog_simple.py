# -*- coding: utf-8 -*-
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
T_BINS=8
# eight bins
step=2*math.pi/T_BINS

print 'step',step

#angle θ ranges from -pi to pi and so should the bins
ANGLE_BINS=[phi for phi in np.arange(-math.pi,math.pi+step,step)]
print 'bins:'
print ANGLE_BINS


def GetAngles(cH,cW,topLeftRow,topLeftCol,L):
    """
    paragraph 4.3
    zero padding on edges
    get angle distribution for a cell
    topLeftRow actual x-coordinate of top left pixel of the cell with respect to L
    topLeftCol actual y-coordinate of top left pixel of the cell with respect to L
    cH ,cW cellHeight,CellWidth
    """


    #print 'Cell dimensions'

    topLeftX=topLeftRow
    topLeftY=topLeftCol

    topRightY=topLeftCol+cW


    lowLeftX=topLeftRow+cH



    H,W=L.shape # H ,W height and width of original image


    #add as many columns as the number of bins
    Cell_Feature=[]
    for b in xrange(0,int(T_BINS)):
        Cell_Feature.append(0)

    Gx=Gy=0L

    for x in xrange(topLeftX,lowLeftX):
        for y in xrange(topLeftY,topRightY):

            #check off limits  add zero
            if x==H-1:
                Gx=-L[x-1][y]
            elif x==0:
                Gx=L[x+1][y]
            else:
                Gx=L[x+1][y]-L[x-1][y]

            #check off limits  add zero

            if y==W-1:
                Gy=-L[x][y-1]
            elif y==0:
                Gy=L[x][y+1]
            else:
                Gy=L[x][y+1]-L[x][y-1]

            Mxy=math.sqrt(Gx**2 + Gy**2)
            Thetaxy=math.atan2(Gy,Gx)

            #print Gx,Gy,Mxy,Thetaxy
            #so we have contribution to
            #Thetaxy is denoted as θ in the paper
            #find the the closest bin to θ


            #Figure 3 page 4
            LeftBin=None #index of closest bin to Thetaxy that is denoted as a in the paper
            RightBin=None

            #Since we have 8 angles LeftBin should be a multiple of PI/4


            for k in xrange(0,len(ANGLE_BINS)):
                #find the largest k for which...

                if ANGLE_BINS[k]<=Thetaxy and ANGLE_BINS[k+1]>=Thetaxy:
                    LeftBin=k
                    RightBin=k+1
                    #print k






            #get the contributions

            # contribution of Mxy[1-a*T_Bins/(2pi) to bin a
            alpha=ANGLE_BINS[RightBin]-Thetaxy

            Cell_Feature[LeftBin]+=Mxy*(1.0-(T_BINS*alpha)/(2*math.pi))

            # contribution of Mxy[T_Bins*a/(2pi) to bin 2*pi/T_Bins-a
            Cell_Feature[RightBin]+=Mxy*T_BINS*alpha/(2*math.pi)








    return Cell_Feature






def DecomposeToCells(Start,End,CH,CW,Conv):
    """
    Window image
    Start : start column of window
    End : end column of window
    Cell Height Cell Width
    Conv Original image convoluted with a smoothing filter
    Ipsos,Platos Original Image dimensions
    """

    Ipsos,Platos=Conv.shape # Original Image dimensions


    Window_Feats=[]

    #covers all the image  for simplicity
    #get all cells
    for sRow in xrange(0,Ipsos,CH):
        for sCol in xrange(Start,End,CW):




                Cell_Features= GetAngles(CH,CW,sRow, sCol,Conv)

                #append Cell_Feature to Window_Feature


                for cf in Cell_Features:
                    Window_Feats.append(cf)


    #normalize according to sum
    s=0.0
    for wf in Window_Feats:
        s+=wf

    for i in xrange(0,len(Window_Feats)):
        Window_Feats[i]=Window_Feats[i]/float(s)


    #this should have a length of Vec_dimensions
    #print 'mikos window feats',len(Window_Feats)
    return Window_Feats




def main():


    img = cv2.imread('pennywise.png',cv2.CV_LOAD_IMAGE_GRAYSCALE)
    ret,img = cv2.threshold(img,0,255,cv2.THRESH_OTSU)


    H, W = img.shape

    print H, W
    cv2.imshow('It',img)
    cv2.waitKey()
    cv2.destroyAllWindows()

    # create Windows with step 5 no overlap
    for i in xrange(0,H , window_Step):
        for j in xrange(0,W , window_Step):
            print 'Window starts at',i,j
            # numpy slice
            win = 
if __name__=="__main__":
    main()


