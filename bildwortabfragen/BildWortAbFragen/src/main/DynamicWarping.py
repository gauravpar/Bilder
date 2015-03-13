import cv2,math
from DTWFeature import DTWFeature

class EventHorizon:


    def __init__(self):
        '''
        Constructor
        '''
        
    def SimpleDynTimeWarp(self,s,t,Band_Width):
        #LGH Features are used here 
        #len(a) rows
        #len (b) cols
        # T. Rath R.Manmatha Word Spotting for Historical Document page 16
                        
        #PRunning Method!!!!
        #s is the synthetic 
        #t is always real
        
        #if the one is less than 65% of the other return inf
        if len(t)>len(s) and len(s)/float(len(t))<0.65: 
            # print 'skip'
            return float("inf")
        elif len(s)>len(t) and len(t)/float(len(s))<0.65:
            # print 'skip'
            return float("inf")
        else:
           
            #print 'mikos s',len(s)
            #print 'mikos t',len(t)
      
            #print 'similar size'
            
            #initialize matrix
            
            
            DTW= [[0 for y in xrange(len(t))] for x in xrange(len(s))] #s rows t columns

                
                
            DTW[0][0]=self.SimpleCost(s[0],t[0])    
                
            for i in xrange(1,len(s)):
                DTW[i][0]=DTW[i-1][0]+self.SimpleCost(s[i], t[0])
            
            for j in xrange(1,len(t)):
                DTW[0][j]=DTW[0][j-1]+self.SimpleCost(s[0], t[j])
                
                
            
        
            #Sakoe-Chiba band
            #get a fraction of the rows size
            R=min(Band_Width,len(s))
            #print 'band',R
              
            #Calculate Cost Matrix
            
            for i in xrange(2,len(s)):
                for j in xrange(2,len(t)):
                    if abs(j-i)>R: 
                        DTW[i][j]=float("inf")
                    else:     
                        cost=self.SimpleCost(s[i],t[j])
                        #print 'cost',cost
                        #Local Constraints
                        #Dynamic Programming Algorithm Optimization for Spoken Word Recognition page 47
                        DTW[i][j]=cost+min(DTW[i-1][j],DTW[i][j-1],DTW[i-1][j-1])
            
                        
    
    
            kost=DTW[len(s)-1][len(t)-1]/float(len(s) + len(t)) #Normalize with the sum of series len
           
            return kost   
        
            
        
    def SimpleCost(self,a,b):
        #a and b are numbers
        return (a-b)**2.0
        
            
    
    
    
    
    def Euclides(self,a,b):
        #a and b are n-dimensional numbers
        return   (a.Top-b.Top)**2 + (a.Low-b.Low)**2 # + (a.Ink-b.Ink)**2 (a.BlackPixels-b.BlackPixels)**2 + 

    
    
    
    
    
    
    def getFeatures(self,Image_Path):
        #S_Path,T_Path are image file paths
        #for each of their columns get three features ,vert project,top,low profile
        Img_Array=cv2.imread(Image_Path,cv2.CV_LOAD_IMAGE_GRAYSCALE)
        ret,Img_Bin=cv2.threshold(Img_Array,0,255,cv2.THRESH_OTSU)
        S_H,S_W=Img_Bin.shape
        
        
        
        
        
       
        #Series_Project=self.getProjection(Img_Bin, S_H,S_W)
        Series_Top=self.getTopProfile(Img_Bin,S_H, S_W)
        #Series_Low=self.getLowProfile(Img_Bin,S_H, S_W)
        #Series_Melani=self.getBackgroundToInk(Img_Bin, S_H, S_W)
        
        #normalize all
       # Series_Project=self.Normalize(Series_Project)
        Series_Top=self.Normalize(Series_Top)
        #Series_Low=self.Normalize(Series_Low)
       # Series_Melani=self.Normalize(Series_Melani)
     
        #print 'len project',len(Series_Project)
        print 'len top',len(Series_Top)
        #print 'len low',len(Series_Low)
        #print 'len melani',len(Series_Melani)
        
    
        series=[]
        
        for i in xrange(0,len(Series_Top)):
            tmp=DTWFeature(0,Series_Top[i],0,0)
            series.append(tmp)
        
        return series
     
     
     
    def getSingleFeature(self,Image_Path):
        #S_Path,T_Path are image file paths
        #for each of their columns get three features ,vert project,top,low profile
        Img_Array=cv2.imread(Image_Path,cv2.CV_LOAD_IMAGE_GRAYSCALE)
        ret,Img_Bin=cv2.threshold(Img_Array,0,255,cv2.THRESH_OTSU)
        S_H,S_W=Img_Bin.shape
        
        
        
        
        
       
        #Series_Project=self.getProjection(Img_Bin, S_H,S_W)
        Series_Top=self.getTopProfile(Img_Bin,S_H, S_W)
        #Series_Low=self.getLowProfile(Img_Bin,S_H, S_W)
        #Series_Melani=self.getBackgroundToInk(Img_Bin, S_H, S_W)
        
        #normalize all
       # Series_Project=self.Normalize(Series_Project)
        Series_Top=self.Normalize(Series_Top)
        #Series_Low=self.Normalize(Series_Low)
       # Series_Melani=self.Normalize(Series_Melani)
     
        #print 'len project',len(Series_Project)
        print 'len top',len(Series_Top)
        #print 'len low',len(Series_Low)
        #print 'len melani',len(Series_Melani)

        return Series_Top
    
    def Normalize(self,unscaled):
        mx=0
        for v in unscaled:
            if v>mx:
                mx=v
    
        
        if mx>0:
            for i in xrange(0,len(unscaled)):
                unscaled[i]=unscaled[i]/float(mx)
        
 
        return unscaled
    
    def getBackgroundToInk(self,Img_Array,Height,Width):
        Ink=[]
        
        #count transitions from 0 to 255
        for col in xrange(0,Width):
            trans=0
            for row in xrange(0,Height-1):
                if Img_Array[row][col]==0 and Img_Array[row+1][col]==255: # White is 255
                    trans+=1
                
            Ink.append(trans)
        
       
        return Ink
    
    def getProjection(self,Img_Array,Height,Width):
        
        Vert=[] # count the  black pixels

        for col in xrange(0,Width):
            sum=0

            for row in xrange(0,Height):
        
                if Img_Array[row][col]==0: #count the BLACK
                    sum+=1
                    
        
            Vert.append(sum)
        return Vert



 
    
    
    def getLowProfile(self,Img_Array,Height,Width):
        #get top profile for dynamic time warping
        #for each column get the coordinates of the first black pixel (aka pixel with highest x coord)


        Low=[] 

        
        for col in xrange(0,Width):
            Low.append(0) #if there are no black pixels in that column we add a zero
            for row in reversed(xrange(0,Height)):
        
                if Img_Array[row][col]==0: #count the BLACK
                    Low[col]=row # Without the Height it is a mirror image of the top profile
                    
                    #print 'a black pixel was found at',row,col
                    break
            else:
                continue
        return Low
    
    

    def getTopProfile(self,Img_Array,Height,Width):
        #get top profile for dynamic time warping
        #for each column get the coordinates of the first black pixel (aka pixel with lowest x coord)


        Top=[] 
        

        
        for col in xrange(0,Width):
            Top.append(0)
            for row in xrange(0,Height):
        
                if Img_Array[row][col]==0: #count the BLACK
                    Top[col]=row # Without the Height it is a mirror image of the top profile
                  
                    #print 'a black pixel was found at',row,col
                    break
            else:
                continue
        return Top


      