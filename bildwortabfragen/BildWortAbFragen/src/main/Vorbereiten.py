import cv2,math
import numpy as np
from skimage import transform,io
from skimage.transform._geometric import AffineTransform

class Vorbereiten:
    '''
    Normalization steps
    '''


    def __init__(self):
        '''
        Constructor
        '''
     
     
        
            
 
    def deslant(self,InputFile,OutputFile,ShearAngles):    
        #Based on the following paper: Frank de Zeeuw Slant Correction using Histograms
        n=6
        
        max_avg_height=0
        goodAngle=0
        
        #for each angle shear the image calculate all local maxima get
        
        
        
        SlantedPic=cv2.imread(InputFile,cv2.CV_LOAD_IMAGE_GRAYSCALE)
        
        ret,SlantedPic=cv2.threshold(SlantedPic,0,255,cv2.THRESH_OTSU)
        
        
        H,W=SlantedPic.shape
        
        
        
        
        for a in ShearAngles:
        
            #print '-------------------------------'
            #print 'Shear by',a
            #shear the image
            ShearMatrix=AffineTransform(matrix=None,scale=None,rotation=None,shear=a)
            
            
            Sheared=transform.warp(SlantedPic,ShearMatrix,cval=1) #pad with whites...
            
             

                  
            
            Ys=[]
            Peaks=[]
            
            HorX=[] #for each column
            
            #calculate the vertical projection
            #count the black pixels in each column
            for col in xrange(0,W):
                sum=0
                for row in xrange(0,H):
                    if Sheared[row][col]==0:
                        sum+=1
                Ys.append(sum)


            #get local maxima...
            for i in xrange(1,len(Ys)-1):
                #if a point is higher than the previous and the  next point
                if Ys[i]>Ys[i-1] and Ys[i]>Ys[i+1]:
                    Peaks.append(Ys[i])
            
            
            #sort descending order the peaks!
          
            #print Ys
            Peaks.sort(reverse=True)
            #print 'Out of',len(Ys),'points we found',len(Peaks),'local maxima'
            

              
            numOfPeaks=len(Peaks) 
            #len(Peaks) can be zero  ....
            if len(Peaks)>0:
                #if less than n peaks return the average of those available   
                #else divide by n
                             
                
                #get the average height of the first n elements
                sum=0
    	    
                for j in xrange(0,min(n,numOfPeaks)):
                    sum+=Peaks[j]
                    
                    
                # print 'sum is ',sum
                # print 'avg height is',sum/float(n)
                
                avg=sum/float(min(n,numOfPeaks))
                print 'shear angle',a,'peaks',len(Peaks),'avg',avg 
                
                if avg>=max_avg_height:
                    max_avg_height=avg
                    print 'peaks',numOfPeaks,'angle',a,'avg height',max_avg_height

                    goodAngle=a
                
                
        print 'shear angle should be ',goodAngle
        
        
        ShearMatrix=AffineTransform(matrix=None,scale=None,rotation=None,shear=goodAngle)
            
        #Shear the original Pic!!!!
        Sheared=transform.warp(SlantedPic,ShearMatrix,cval=1) #pad with whites...
            
      
       
        #save that
        io.imsave(OutputFile, Sheared)
        #cv2.imshow('Deslanted',Sheared)
        #cv2.waitKey()
        #cv2.destroyAllWindows()


    def Crop(self,InputFile,OutputFile):



        #all white rows and cols 
    
        img=cv2.imread(InputFile,cv2.CV_LOAD_IMAGE_GRAYSCALE)
        ret,img_bin=cv2.threshold(img,0,255,cv2.THRESH_OTSU)
        
        H,W=img_bin.shape
        
        #print 'Ypsos',H,'platos',W
        TopRow=H
        BottomRow=0
        LeftCol=0
        RightCol=W
        
        
        #ahh these histograms again
        #compute vertical and horizontal histograms  almost
        
        
        
        
        #keep reading columns until you find one that has a black pixel
        found=0
        
        while LeftCol<W and found==0:
            
            r=0
            while r<H and found==0:
                
                #print r,LeftCol
                if img_bin[r][LeftCol]==0:
                    found=1
                r+=1
            LeftCol+=1
               
        LeftCol-=1
        
        
        
        found=0
        
        while RightCol>0 and found==0:
            RightCol-=1
            r=0
            while r<H and found==0:
                
                #print r,RightCol
                if img_bin[r][RightCol]==0:
                    found=1
                r+=1
            
               
        RightCol+=1
        
        
        
        found=0
        #you need to find the lowest black pixel
        
        for r in xrange(0,H):
            for c in xrange(0,W):
                if img_bin[r][c]==0 and r<TopRow:
                    TopRow=r
        
        TopRow-=1
        
        found=0
        #you need to find the  black pixel with the highest row
        
        for r in xrange(0,H):
            for c in xrange(0,W):
                if img_bin[r][c]==0 and r>BottomRow:
                    BottomRow=r
        
        BottomRow+=1
        #print 'Bounding box is : LeftCol',LeftCol,'RightCol',RightCol,'TopRow',TopRow,'BottomRow',BottomRow
        
        
        #save the image to a new location
        Cropped=np.ones((BottomRow-TopRow,RightCol-LeftCol,1), np.uint8)
        Cropped.fill(255)
        
        i=-1
        for r in xrange(TopRow,BottomRow):
            i+=1
            j=-1
            for c in xrange(LeftCol,RightCol):
                j+=1
                Cropped[i][j]=img_bin[r][c]
                
                
          
        cv2.imwrite(OutputFile,Cropped,[cv2.IMWRITE_PNG_COMPRESSION,95])
        

    def Scale(self,InputFile,FixedHeight):
       
        img=cv2.imread(InputFile,cv2.CV_LOAD_IMAGE_GRAYSCALE)
        ret,im_bin=cv2.threshold(img,0,255,cv2.THRESH_OTSU)
        if FixedHeight>0:        
            H,platos=im_bin.shape
            
            scale_fact_y=FixedHeight/float(H)
            print 'new width',platos*scale_fact_y # this is the new width!!!
            
            
            return cv2.resize(im_bin,None,fx=scale_fact_y,fy=scale_fact_y,interpolation=cv2.INTER_CUBIC)
        else:
            return im_bin
    
    
    #Alessandro Vinciarelli *, Juergen Luettin deslanting

    def HCol(self,picArr,col):
        #Calculates the amount of black pixels in column col
        H,W=picArr.shape

        hm=0
        for row in xrange(0,H):
            if picArr[row][col]==0:
                hm+=1.0
    
        return float(hm)



    def DeltaCol(self,picArr,col):
    #Calculates the distance of first and last black pixel in column col
        H,W=picArr.shape
        #print 'Height',H,'Width',W
        #first pixel
        first=0
        
        while picArr[first][col]!=0 and first<H-1:
            #print 'first',first
            first+=1
            
            
        last=H-1
        while picArr[last][col]!=0 and last>0:
            last-=1
            
            
        #print 'first',first,'last',last
        return float(math.fabs(last-first))



    def Vinciarelli(self,InputFile,OutputFile,ShearAngles):
        #Load an image and shear it
        SlantedPic=cv2.imread(InputFile,cv2.CV_LOAD_IMAGE_GRAYSCALE)
        ret,SlantedPic=cv2.threshold(SlantedPic,0,255,cv2.THRESH_OTSU)
    
        
        H,W=SlantedPic.shape
        
        maxS=0
        goodAngle=0
        
        for a in ShearAngles:
            #print 'shear by',a
            
            ShearMatrix=AffineTransform(matrix=None,scale=None,rotation=None,shear=a)
            
            
            Sheared=transform.warp(SlantedPic,ShearMatrix,cval=1) #pad with whites...
            
            S_a=0
            
            #for each column calc h/D

            for col in xrange(0,W):
                h_a=self.HCol(Sheared, col)
                if h_a!=0: #there are some black pixels in that column...
                    #so we can calculate D_a
                    D_a=self.DeltaCol(Sheared, col)
                
                    #print 'h_a',h_a,'d_a',D_a

                #if this one sum h_a**2
                
                    if h_a==D_a:
                        #print 'we found a col!!'
                        S_a+=h_a*h_a
                    
                
            
            
            if S_a>maxS:
                maxS=S_a
                goodAngle=a
            
                
        print 'Optimal Shear by',goodAngle
        ShearMatrix=AffineTransform(matrix=None,scale=None,rotation=None,shear=goodAngle)
            
        #Slant OriginalPic    
        Sheared=transform.warp(SlantedPic,ShearMatrix,cval=1) #pad with whites...
        
        io.imsave(OutputFile, Sheared)
