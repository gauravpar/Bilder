'''
Created on Aug 19, 2014

@author: phoenix
'''
import sys,csv,os.path,math,numpy as np,pickle
from sklearn import svm,ensemble

#synthetic query of a font and word is the one class example ???

#read the vector of the example


#read the vectors of the example set

'''
---------------------------------------------
inputs
 synth image file names 
 synth feats
 hand image file names 
 hand feats 
 truth file
---------------------------------------------
'''

        
QueryFeats=[]

HandFileNames=[]
HandFeats=[]
Truth=[]

QueryFeatsTxt='/home/phoenix/Desktop/train_fits.txt'

HandNamesTxt='/home/phoenix/Desktop/test_onomata.txt'
HandFeatsTxt='/home/phoenix/Desktop/test_fits.txt'
HandTruthFile='/home/phoenix/washingtondb-v1.0/ground_truth/word_labels.txt'

KeyWord='Regiment'



HandFileNames=pickle.load(open(HandNamesTxt,'rb'))
HandFeats=pickle.load(open(HandFeatsTxt,'rb'))

QueryFeats=pickle.load(open(QueryFeatsTxt,'rb'))



with open(HandTruthFile,'r') as file:
    for line in file:
        Truth.append(line)


Distances=[]
    
#svm...


MyClassifier=svm.OneClassSVM(nu=0.08, kernel="sigmoid", gamma=0.07,coef0=0.07,degree=4)
MyClassifier.fit(QueryFeats)

print 'predicting...'


TP=TN=FP=FN=0

Remaining=len(HandFileNames)

for i in xrange(0,len(HandFileNames)):
     

    Remaining-=1
    
    
    #print MyClassifier.decision_function(HandFeats[i])              
    
    
    transcript=''
    for line in Truth:
        #print line
        if os.path.basename(HandFileNames[i]).replace('.png','') in line:
            tmp=line.split(' ')
            #print tmp[0],tmp[1]
            transcript=tmp[1].replace('\n','') 
    
    
    y_pred_test = MyClassifier.predict(HandFeats[i])
            
    
    
    if y_pred_test>0:    
        

        if KeyWord in transcript:    
            TP+=1
            Distances.append(MyClassifier.decision_function(HandFeats[i]))

        if KeyWord not in transcript:
            FP+=1
            
    if y_pred_test<0:    
        

        if KeyWord in transcript:    
            FN+=1
        if KeyWord  not in transcript:
            TN+=1
     
    print Remaining,TP,FP,FN,TN

    
print 'acc',(TP+TN)/float(TP+TN+FN+FP)
print 'prec',TP/float(TP+FP)
print 'recall',TP/float(TP+FN)
