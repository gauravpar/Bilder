# -*- coding: utf-8 -*-
import cv2,math,glob,csv
import numpy as np
'''

please FIX IT OUT DATE
        
This should be exatcly the same as hogOverlap
************************ OVERLAPPING WINDOWS ************************
testing histogram of oriented features 8 gradients

arg1 handwritten images
arg2 csv image file
arg3 csv feature file
arg4 window width
arg5 shift percentage


Local Gradient Histogram Features for Word Spotting in Unconstrained Handwritten Documents
J. Rodriguez F.Perronnin
steps according to paper

Apply a smoothing filter and maybe a Gaussian Derivative
Create a sliding window of width w and Height equal to image height
Create 8 cells with equal dimensions in each window
For each cell get an 8 feature vector
For each pixel of the cell calculate Gx,Gy,Thetaxy
Add contributions to the cell vector accordingly
Concatenate the vector for each cell into a empty vector
This vector should have 4*4*8 dimensions
Normalize this vector according to the sum of all its elements NOT by its maximum
Concatenate the normalized vector to the image vector
'''


class FeatExtract:


    def __init__(self,InPutFolder,FeatsFile,ImageFiles,w,d):
        '''
        Constructor
        '''
        
        self.T_BINS=8.0
        # eight bins

        #angle θ ranges from -pi to pi and so should the bins
        self.ANGLE_BINS=[-math.pi,-3.0*math.pi/4.0,-math.pi/2.0,-math.pi/4.0,0,math.pi/4.0,math.pi/2.0,3.0*math.pi/4.0,math.pi]
            
        self.Win_Platos=w
        self.Win_Overlap= self.Win_platos - int(d * self.Win_platos)
        
        print ' window width',self.Win_Platos
        print ' shift by',self.Win_Overlap
            
        print self.ANGLE_BINS
        
        
        files=glob.glob(InPutFolder + '*.*')
        Image_FileNames=[]
        Collection_Feats=[]

    
        for filename in files:
            Image_FileNames.append(filename)
            print 'extracting hog for ',filename
            img=cv2.imread(filename,cv2.CV_LOAD_IMAGE_GRAYSCALE)
            ret,img=cv2.threshold(img,0,255,cv2.THRESH_OTSU)
            
            
            
            H,W=img.shape
            #find that sliding NON -OVERALPING window
            
            
            print 'image width is ',W
  
          
          
          
          
            extra_cols=0
            
      
            arxi=0
            # padding white columns....
            #arxi will contain the last column where we cannot add a window
            while arxi<W:
                #print arxi
                arxi+=self.Win_Overlap
    
                
            
            arxi=arxi-self.Win_Overlap
            #print 'arxi',arxi
    
            extra_cols= arxi+self.Win_platos-W
            print 'added',extra_cols
    
            
            W+=extra_cols
            
            
    
            print 'new image width is ',W
            
            
            
            ext_img= np.ones((H,W,1), np.uint8)
            ext_img.fill(255)
            
            for i in xrange(0,H):
                #copy old image
                for j in xrange(0,W-extra_cols):
                    ext_img[i][j]=img[i][j]
               
              
                
            
            #cv2.imshow('after zeros',ext_img)
            #cv2.waitKey()
            #cv2.destroyAllWindows()
            
          
            
            
            CellHeight=H/4 #H should be be 120
            CellWidth=self.Win_platos/4
                    
            Convol = cv2.blur(ext_img,(5,5))  #smoothing filter #maybe a gradient should be added too
                                         
                                          
        
           
            #get all sliding windows
            StartCol=-self.Win_Overlap
            
            while StartCol+self.Win_platos<W:
                StartCol+=self.Win_Overlap
                print '-----------------------'
               
                #print 'window height from ',0,H
                
                print 'window start col',StartCol,'end col',StartCol+self.Win_platos
            
                #sliding window...
                #Each Window has a height of H equal to the image 's height and Width ranging from StartCol to StartCol+Win_Platos        
        
                
                
            
            
             
                win_arr=np.ones((H,self.Win_platos,1),np.uint8)
                win_arr.fill(255)
                    
             
                
                for r in xrange(0,H):
                    j=-1
                    for c in xrange(StartCol,StartCol+self.Win_platos):
                        j+=1
                        win_arr[r][j]=Convol[r][c]
                            
                
                #cv2.imshow('cell array',win_arr)
                #cv2.waitKey()
                #cv2.destroyAllWindows()
                #for that cell get the angles
                
                
              
                Win_Feats=self.DecomposeToCells(StartCol,StartCol+self.Win_platos,CellHeight,CellWidth,Convol)
                
                
                #Win_Feats is a vector that contains the features for each window...
                #concatenate them to Image_Feature
                Collection_Feats.append(Win_Feats)
                    
        
        
            
            
       
        #write to a csv file
        #file path is sysargv[2]
        #first row should be attribute names
        with open(ImageFiles, 'wb') as CsvFile:    
            CsvWriter= csv.writer(CsvFile,delimiter=',') 
            CsvWriter.writerows(Image_FileNames)
                
                
        
        
        #write to a csv file for Expectation Maximization via Rapid Miner
        #file path is sysargv[4]
        #first row should be attribute names
        with open(FeatsFile, 'wb') as CsvFile:    
            CsvWriter= csv.writer(CsvFile,delimiter=',') 
            CsvWriter.writerows(Collection_Feats)
                
                
       
        

    
                        

        
 
    def GetAngles(self,cH,cW,topLeftRow,topLeftCol,L):
        #paragraph 4.3
        #zero padding on edges
        #get angle distribution for a cell
        #topLeftRow actual x-coordinate of top left pixel of the cell with respect to L
        #topLeftCol actual y-coordinate of top left pixel of the cell with respect to L
        #cH ,cW cellHeight,CellWidth
        
        
        #returns a vector for that cell??
        
        #print 'Cell dimensions'
        
        topLeftX=topLeftRow
        topLeftY=topLeftCol
        
    #    topRightX=topLeftRow
        topRightY=topLeftCol+cW
        
        
        lowLeftX=topLeftRow+cH
    #    lowLeftY=topLeftCol
        
    #    lowRightX=topLeftRow+cH
    #    lowRightY=topLeftCol+cW
        
        #print 'TopLeft',topLeftX,topLeftY
        #print 'TopRight',topRightX,topRightY
        
        #print 'LowLeft',lowLeftX,lowLeftY
        #print 'LowRight',lowRightX,lowRightY
        
        
        H,W=L.shape # H ,W height and width of original image
        
        
        Cell_Feature=[0,0,0,0,0,0,0,0]# 8 rows one for each bin
        
        Gx=Gy=0L
        
        for x in xrange(topLeftX,lowLeftX): #120 last row fix
            for y in xrange(topLeftY,topRightY):
                
                #check off limits 
                if x==H-1:
                    Gx=-L[x-1][y]
                elif x==0:
                    Gx=L[x+1][y]
                else:
                    Gx=L[x+1][y]-L[x-1][y]
                
                #check off limits 
    
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
                
                
                for k in xrange(0,len(self.ANGLE_BINS)):
                    #find the largest k for which...
                    
                    if self.ANGLE_BINS[k]<=Thetaxy and self.ANGLE_BINS[k+1]>=Thetaxy:
                        LeftBin=k
                        RightBin=k+1
                        #print k
                
    
    
                        
               
                
                #get the contributions
                
                # contribution of Mxy[1-a*T_Bins/(2pi) to bin a
                alpha=self.ANGLE_BINS[RightBin]-Thetaxy
                
                Cell_Feature[LeftBin]+=Mxy*(1.0-(self.T_BINS*alpha)/(2*math.pi))
                
                # contribution of Mxy[T_Bins*a/(2pi) to bin 2*pi/T_Bins-a
                Cell_Feature[RightBin]+=Mxy*self.T_BINS*alpha/(2*math.pi)
                
                
                
                
                
                
                
                
        return Cell_Feature        
        
    
                
      
    
            
    def DecomposeToCells(self,Start,End,CH,CW,Conv):
        #Window image 
        #Start : start column of window
        #End : end column of window
        
        #Cell Height Cell Width
        #Conv Original image convoluted with a smoothing filter
        
        Ipsos,Platos=Conv.shape # Original Image dimensions
        
        Window_Feats=[]
        
        #window covers all the image  for simplicity
        #get all cells
        for sRow in xrange(0,Ipsos,CH):        
            for sCol in xrange(Start,End,CW):
                        
                        
                    #create a cell array
                    #copy pixels
                    #cell_arr=np.ones((CH,CW,1),np.uint8)
                    #cell_arr.fill(255)
                        
                    #i=-1
                    
                    #for r in range(sRow,sRow+CH):
                    #    i+=1
                    #    j=-1
                    #    for c in range(sCol,sCol+CW):
                    #        j+=1
                    #        cell_arr[i][j]=Conv[r][c]
                                
                    #
                    #cv2.imshow('cell array',cell_arr)
                    #cv2.waitKey()
                    #cv2.destroyAllWindows()
                    #for that cell get the angles
                    
                    Cell_Features= self.GetAngles(CH,CW,sRow, sCol,Conv)            
                    
                    #append Cell_Feature to Window_Feature            
                                
                        
                    for cf in Cell_Features:
                        Window_Feats.append(cf)
            
            
        #normalize according to sum   
        s=0.0
        for wf in Window_Feats:
            s+=wf
        
        for i in xrange(0,len(Window_Feats)):
            Window_Feats[i]=Window_Feats[i]/float(s)
            
        
        #this should have a length o 128
        #print 'mikos window feats',len(Window_Feats)
        return Window_Feats
        
