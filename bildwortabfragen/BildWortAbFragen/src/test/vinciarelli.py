
import cv2,numpy as np,math
from skimage import transform,io
from skimage.transform._geometric import AffineTransform
#Alessandro Vinciarelli *, Juergen Luettin deslanting


def VertCol(picArr,col):
    #Calculates the amount of black pixels in column col
    H,W=picArr.shape

    hm=0
    
    return hm



def DeltaCol(picArr,col):
    #Calculates the distance of first and last black pixel in column col
    Dm=0
    H,W=picArr.shape

    return Dm



def main():
    #Load an image and shear it
    fname=raw_input('')
    SlantedPic=cv2.imread(fname,cv2.CV_LOAD_IMAGE_GRAYSCALE)
    ret,SlantedPic=cv2.threshold(SlantedPic,0,255,cv2.THRESH_OTSU)
    
    ret,OriginalPic=cv2.threshold(SlantedPic,0,255,cv2.THRESH_OTSU)
    
    H,W=SlantedPic.shape
    
    maxS=0
    goodAngle=0
    
    for a in np.arange(-math.pi/2.8,math.pi/2.8,math.pi/60.0):
        print 'shear by',a
        
        ShearMatrix=AffineTransform(matrix=None,scale=None,rotation=None,shear=a)
        
        
        Sheared=transform.warp(SlantedPic,ShearMatrix,cval=1) #pad with whites...
        #for each column calc h/D
        #if this one sum it
        S_a=0
        
        
        
        if S_a>maxS:
            maxS=S_a
            goodAngle=a
        
            
    print 'Slant by',goodAngle
    ShearMatrix=AffineTransform(matrix=None,scale=None,rotation=None,shear=a)
        
        
    Sheared=transform.warp(SlantedPic,ShearMatrix,cval=1) #pad with whites...
    
    
if __name__=='__main__':
    main()