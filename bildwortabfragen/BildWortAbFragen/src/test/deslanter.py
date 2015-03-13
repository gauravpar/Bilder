'''
Created on Jul 9, 2014

@author: phoenix
'''
#try to deslant vertical histogram count peak aka local maxima height
import cv2,math
import sys
import numpy as np
from skimage import transform,io
from skimage.transform._geometric import AffineTransform
import glob
n=3


InPath=sys.argv[1] + '*.*'
OutPath=sys.argv[2]





print 'inpath is ',InPath
print 'outpath is ',OutPath



#for each angle shear the image calculate all local maxima get

files=glob.glob(InPath)


for fname in files:
    
    print '-------------------------------'
    print fname
    #get the word name along with the font
    inx=fname.rindex('synth') +6
    Word_Name=fname[inx:]    
    Word_Name=Word_Name.replace('.png','')
    Word_Name='synth_'+Word_Name
    print 'Word name is',Word_Name    
    
    max_avg_height=0
    goodAngle=0

    
    SlantedPic=cv2.imread(fname,cv2.CV_LOAD_IMAGE_GRAYSCALE)
    ret,SlantedPic=cv2.threshold(SlantedPic,0,255,cv2.THRESH_OTSU)
    H,W=SlantedPic.shape
    
    
 
    ShearAngles=[]
    ShearAngles.append(0) #calculate histogram at the original image...
    for a in np.arange(-math.pi/4.0,math.pi/4.0,math.pi/60.0): #this should be be in radians!!! 3 degrees loop
        ShearAngles.append(a)
        
    for a in ShearAngles:
        
        
        #print 'Shear by',a
        #shear the image
        ShearMatrix=AffineTransform(matrix=None,scale=None,rotation=None,shear=a)
        
        
        Sheared=transform.warp(SlantedPic,ShearMatrix,cval=1) #pad with whites...
        
        
        
        
        Ys=[]
        Peaks=[]
        #calculate the vertical projection
        #count the black pixels in each column
        for col in xrange(0,W):
            sum=0
            for row in xrange(0,H):
                if Sheared[row][col]==0:
                    sum+=1
            Ys.append(sum)
            
        #get local maxima
        for i in xrange(1,len(Ys)-1):
            if Ys[i]>Ys[i-1] and Ys[i]<Ys[i+1]:
                Peaks.append(Ys[i])
        
        
        #sort descending order the peaks!
      
        
        Peaks.sort(reverse=True)
        #print 'Out of',len(Ys),'points we found',len(Peaks),'local maxima'
        
        #get the average height of the first n elements
            

                
        numOfPeaks=len(Peaks) 
        #len(Peaks) can be zero  ....
        if len(Peaks)>0:
            #if less than n peaks return the average of those available   
            #else divide by n 
            if numOfPeaks>n:
                numOfPeaks=n
                #get the average height of the first n elements
            sum=0
            
            for j in xrange(0,min(n,len(Peaks))):
                sum+=Peaks[j]
                
                
            print 'peaks',numOfPeaks,'angle',a 
            
            
    print 'shear angle should be ',goodAngle
    
    
    ShearMatrix=AffineTransform(matrix=None,scale=None,rotation=None,shear=goodAngle)
        
        
    Sheared=transform.warp(SlantedPic,ShearMatrix,cval=1) #pad with whites...
        
    
        
        
    #cv2.imshow('Deslanted',Sheared)
    #cv2.waitKey()
    #cv2.destroyAllWindows()
    
    io.use_plugin('pil')
    io.imsave(OutPath + Word_Name+ '.png',Sheared)
