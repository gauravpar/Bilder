# -*- coding: utf-8 -*-
import cv2,math,glob,sys,csv
import numpy as np


''''
Local Gradient Histogram Features for Word Spotting in Unconstrained Handwritten Documents
J. Rodriguez F.Perronnin


arg1  image folder
arg2 csv image filenames
arg3 csv feature file
arg4 window width
arg5 overlap
arg6 cells in each dimension this should be 2 if four crash...
arg7 number of Bins can only be above 5 ....
arg8 params file



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


T_BINS=float(sys.argv[7])
# eight bins
vima=2*math.pi/T_BINS

print 'vima',vima

#angle θ ranges from -pi to pi and so should the bins
ANGLE_BINS=[]

for phi in np.arange(-math.pi,math.pi+vima,vima):
    ANGLE_BINS.append(phi)
            
Remaining=None            
print ANGLE_BINS


def GetAngles(cH,cW,topLeftRow,topLeftCol,L):
    #paragraph 4.3
    #zero padding on edges
    #get angle distribution for a cell
    #topLeftRow actual x-coordinate of top left pixel of the cell with respect to L
    #topLeftCol actual y-coordinate of top left pixel of the cell with respect to L
    #cH ,cW cellHeight,CellWidth
    
    
    
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
    #Window image 
    #Start : start column of window
    #End : end column of window
    
    #Cell Height Cell Width
    #Conv Original image convoluted with a smoothing filter
    
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
    files=glob.glob(sys.argv[1]+ '*.*')
    Collection_Feats=[]
    
    #dimension of each vector=cells in each window * bins
    Vector_Dim=int(4*T_BINS)*int(sys.argv[6])
    print 'vector dimensions',Vector_Dim
    Image_FileNames=[]

    #start row and end row of feature vector
    sV=eV=0
        
    Remaining=len(files)


    for filename in files:
        Csv_Row=[] #first row img name second 1st row of vectors 3rd row last vectors
        
        
        Remaining-=1
        
        print 'extracting hog for ',filename
        img=cv2.imread(filename,cv2.CV_LOAD_IMAGE_GRAYSCALE)
        ret,img=cv2.threshold(img,0,255,cv2.THRESH_OTSU)
        
        print 'remaining',Remaining
        
        H,W=img.shape
        #find that sliding NON -OVERALPING window
        
        
        #print 'image width is ',W
        
        #16 cells per window
        
        
        
        #Window width
        Win_platos=int(sys.argv[4])
        
        #win overlap is float(sys.argv [5])
        # it means how many columns we are going to shift to the left the window
        Win_Overlap= Win_platos - int(float(sys.argv[5]) * Win_platos)
        
        #print 'shift windows by',Win_Overlap
         
        
        
        #cv2.imshow('before zeros',img)
        #cv2.waitKey()
        #cv2.destroyAllWindows()
        
        
        
      
      
      
      
      
        extra_cols=0
        
        print 'old image width is ',W

  
        arxi=0
        # padding white columns....
        #arxi will contain the last column where we cannot add a window
        while arxi<W:
            #print arxi
            arxi+=Win_Overlap

            
        
        arxi=arxi-Win_Overlap
        #print 'arxi',arxi

        extra_cols= arxi+Win_platos-W
        #print 'added',extra_cols

        
        W+=extra_cols
        
        #add extra cols so that number of cells is divisible by height
        
        print 'new image width is ',W
        
        print 'old image height in ',H

        #padding white rows
        #the new height should be divisible by sys.argv[6]
        
        extra_rows=0



        while H % int(sys.argv[6])!=0:
            H+=1
            extra_rows+=1
        
        print 'new image height in ',H
        
        
        
        ext_img= np.ones((H,W,1), np.uint8)
        ext_img.fill(255)
        
        for i in xrange(0,H-extra_rows):
            #copy old image
            for j in xrange(0,W-extra_cols):
                ext_img[i][j]=img[i][j]
           
          
            
        
      
        
        #two by two cells
        print 'cells in each dimensions',sys.argv[6]
        
        CellHeight=H/int(sys.argv[6])  #H should be divisible by CellHeight
        
        CellWidth=Win_platos/int(sys.argv[6])
                
        Convol = cv2.blur(ext_img,(5,5))  #smoothing filter 
        
        #maybe a gradient should be added too
        
                                     
           
        #cv2.imshow('after zeros',Convol)
        #cv2.waitKey()
        #cv2.destroyAllWindows()
                                   
    
       
        #get all sliding windows
        StartCol=-Win_Overlap
        
        
        while StartCol+Win_platos<W:
            StartCol+=Win_Overlap
            #print '-----------------------'
            
            eV+=1
                       
        
            #print 'window height from ',0,H
            
            #print 'window start col',StartCol,'end col',StartCol+Win_platos
        
            #sliding window...
            #Each Window has a height of H equal to the image 's height and Width ranging from StartCol to StartCol+Win_Platos        
    
            
            
        
        
         
            win_arr=np.ones((H,Win_platos,1),np.uint8)
            win_arr.fill(255)
                
         
            
            for r in xrange(0,H):
                j=-1
                for c in xrange(StartCol,StartCol+Win_platos):
                    j+=1
                    win_arr[r][j]=Convol[r][c]
                        
            
            #cv2.imshow('cell array',win_arr)
            #cv2.waitKey()
            #cv2.destroyAllWindows()
            #for that cell get the angles
            
            
          
            Win_Feats=DecomposeToCells(StartCol,StartCol+Win_platos,CellHeight,CellWidth,Convol)
            
            
            #Win_Feats is a vector that contains the features for each window...
            #concatenate them to Image_Feature
            Collection_Feats.append(Win_Feats)
                    
            
    
        
        
        Csv_Row=[filename,sV,eV]
        print Csv_Row
        sV=eV+1 # the vector of the next image starts at sV
        Image_FileNames.append(Csv_Row)        
        
   
    #write to a csv file
    #file path is sysargv[2]
    #first row should be attribute names
    with open(sys.argv[2], 'wb') as CsvFile:    
        CsvWriter= csv.writer(CsvFile,delimiter=',') 
        CsvWriter.writerows(Image_FileNames)
            
            
                     
       
 
    
   
    
    
    
    #write Collections feats to an csv file
    with open(sys.argv[3], 'wb') as CsvFile:    
        CsvWriter= csv.writer(CsvFile,delimiter=',') 
        CsvWriter.writerows(Collection_Feats)
            
    
    
       
    file=open(sys.argv[8],'w')
    file.write('window width ' + sys.argv[4] + '\n')
    file.write('window overlap ' + sys.argv[5] + '\n')
    file.write('cell width ' + sys.argv[6] + '\'n')
   
    file.write('bins ' + sys.argv[7] + '\n')
    file.close()
    
    
    
    
    
if __name__=="__main__":
    main() 
 
 