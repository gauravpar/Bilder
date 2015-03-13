import glob,cv2,os,pickle,numpy as np,csv


#find the max from synthetic and handwritten

#http://scikit-image.org/docs/dev/auto_examples/plot_hog.html

TrainSetPics=glob.glob('/home/phoenix/Desktop/full_synth/*.png')
TestSetPics=glob.glob('/home/phoenix/washingtondb-v1.0/data/word_images_normalized/*.png')


Truth=[]


with open('/home/phoenix/washingtondb-v1.0/ground_truth/word_labels.txt','r') as file:
    for line in file:
        Truth.append(line)




  

TestNames=[]
TestFeats=[]

TrainNames=[]
TrainFeats=[]

TrainFeats.append(['h1','h2','h3','h4','h5','h6','h7','class'])
TestFeats.append(['h1','h2','h3','h4','h5','h6','h7','class'])


KeyWord='Regiment'


Remaining=len(TestSetPics) + len(TrainSetPics)
for test in TestSetPics:
    image=cv2.imread(test,cv2.CV_LOAD_IMAGE_GRAYSCALE)
    ret,image=cv2.threshold(image,0,255,cv2.THRESH_OTSU)
   
    Remaining-=1

    print 'remaining',Remaining
   
    TestNames.append(os.path.basename(test)) 

    ropes=cv2.moments(image,False)
    hu=cv2.HuMoments(ropes)





    transcript=''
    for line in Truth:
        #print line
        if os.path.basename(test).replace('.png','') in line:
            tmp=line.split(' ')
            #print tmp[0],tmp[1]
            transcript=tmp[1].replace('\n','') 
            print transcript
            
            
    ropes=[]
    
    for i in range(0,len(hu)):
        ropes.append(float(hu[i]))
    if KeyWord in transcript:
        ropes.append(KeyWord)
    else:
        ropes.append('Nothing')    
    TestFeats.append(ropes)
    
   


pickle.dump( TestNames, open('/home/phoenix/Desktop/test_onomata.txt', "wb" ) )
pickle.dump( TestFeats, open('/home/phoenix/Desktop/test_fits.txt', "wb" ) )


for train in TrainSetPics:
    image=cv2.imread(train,cv2.CV_LOAD_IMAGE_GRAYSCALE)
    ret,image=cv2.threshold(image,0,255,cv2.THRESH_OTSU)
    
  
    Remaining-=1

    ropes=cv2.moments(image,False)
    hu=cv2.HuMoments(ropes)   
    print 'remaining',Remaining
    
    ropes=[]
    for i in range(0,len(hu)):
        ropes.append(float(hu[i]))
   
    ropes.append(KeyWord)
    print ropes
    TrainNames.append(os.path.basename(train)) 
    TrainFeats.append(ropes)
    



pickle.dump( TrainNames, open('/home/phoenix/Desktop/train_onomata.txt', "wb" ) )
pickle.dump( TrainFeats, open('/home/phoenix/Desktop/train_fits.txt', "wb" ) )



    
#write Collections feats to an csv file
with open('/tmp/synth.csv', 'wb') as CsvFile:    
    CsvWriter= csv.writer(CsvFile,delimiter=',') 
    CsvWriter.writerows(TrainFeats)
    

#write Collections feats to an csv file
with open('/tmp/hand.csv', 'wb') as CsvFile:    
    CsvWriter= csv.writer(CsvFile,delimiter=',') 
    CsvWriter.writerows(TestFeats)
    
            
    
    

