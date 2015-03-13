from skimage.feature import hog

import glob,cv2,os,pickle,numpy as np



#http://scikit-image.org/docs/dev/auto_examples/plot_hog.html

TrainSetPics=glob.glob('/home/phoenix/Desktop/handcraft/queries/*.png')
TestSetPics=glob.glob('/home/phoenix/washingtondb-v1.0/data/word_images_normalized/*.png')



TestNames=[]
TestFeats=[]

TrainNames=[]
TrainFeats=[]

Remaining=len(TestSetPics) + len(TrainSetPics)
for test in TestSetPics:
    image=cv2.imread(test,cv2.CV_LOAD_IMAGE_GRAYSCALE)

    fd = hog(image, orientations=6, pixels_per_cell=(16, 16),
                    cells_per_block=(1, 1), visualise=False,normalise=True)
    Remaining-=1

    print 'remaining',Remaining
   
    TestNames.append(os.path.basename(test)) 
    arr=np.array(fd,dtype=np.float64)

    TestFeats.append(arr)
    
   


pickle.dump( TestNames, open('/home/phoenix/Desktop/test_onomata.txt', "wb" ) )
pickle.dump( TestFeats, open('/home/phoenix/Desktop/test_fits.txt', "wb" ) )


for train in TrainSetPics:
    image=cv2.imread(train,cv2.CV_LOAD_IMAGE_GRAYSCALE)

    fd= hog(image, orientations=6, pixels_per_cell=(16, 16),
                    cells_per_block=(1, 1), visualise=False,normalise=True)
    Remaining-=1

    arr=np.array(fd,dtype=np.float64)
    print 'remaining',Remaining
   
    TrainNames.append(os.path.basename(train)) 
    TrainFeats.append(arr)
    



pickle.dump( TrainNames, open('/home/phoenix/Desktop/train_onomata.txt', "wb" ) )
pickle.dump( TrainFeats, open('/home/phoenix/Desktop/train_fits.txt', "wb" ) )



