'''
Created on Aug 16, 2014

@author: phoenix
'''
import sys,math,pickle,mlpy,os,pickle

#platos zonis 50
#zoni SC


SetOneNames=pickle.load(open(sys.argv[1],'rb'))
SetOneFeats=pickle.load(open(sys.argv[2],'rb'))

MaximumScore=6 
AvgScore=0

HandGroundTruth=[]
with open(sys.argv[3],'r') as file:
    for line in file:
        HandGroundTruth.append(line)


SetTwoNames=pickle.load(open(sys.argv[1],'rb'))
SetTwoFeats=pickle.load(open(sys.argv[2],'rb'))

Comps=len(SetTwoNames)**2

for q in xrange(0,len(SetOneNames)):
    transcipt=''
    
    for line in HandGroundTruth:
        if transcipt.replace('.png','') in line:
                tmp=line.split(' ')                         
                transcipt=tmp[1].replace('\n','')

    RetrievedWords=[] #retrieved word transcript
    RetrievedScore=[] #score matching
    

    
    for w in xrange(0,len(SetTwoNames)):
        
        Comps-=1
        
        dist=1000
        if len(SetTwoFeats[w])>len(SetOneFeats[q]) and len(SetOneFeats[q])/float(len(SetTwoFeats[w]))<0.65: 
                # print 'skip'
                dist=float("inf")
        elif len(SetOneFeats[q])>len(SetTwoFeats[w]) and len(SetTwoFeats[w])/float(len(SetOneFeats[q]))<0.65:
                # print 'skip'
                dist=float("inf")
        else:
           
           
               
            dist,cost,path=mlpy.dtw_std(SetTwoFeats[w],SetOneFeats[q], dist_only=False, metric='euclidean', constraint='slanted-band', k=50)
                
        
                
            dist=dist/float(len(SetOneFeats[q]) + len(SetTwoFeats[w]))
            
            res_transcript=''
            for line in HandGroundTruth:
                if SetTwoNames[w].replace('.png','') in line:
                    tmp=line.split(' ')                         
                    res_transcipt=tmp[1].replace('\n','')
        
            print 'query with image',SetOneNames[q],'inscribed',transcipt,'retrieved word ',res_transcipt,'with score ',dist
            print 'remaining ',Comps

            RetrievedScore.append(dist)
            RetrievedWords.append(res_transcript)
    
    #sort ascending by retrieved score
    
    RetrievedScore, RetrievedWords = (list(x) for x in zip(*sorted(zip(RetrievedScore, RetrievedWords), key=lambda pair: pair[0])))
    
    query_score=0
    
    
    print RetrievedWords[0],RetrievedScore[0]
    print RetrievedWords[1],RetrievedScore[1]
    print RetrievedWords[2],RetrievedScore[2]
    

    if transcipt in RetrievedWords[0]:
        query_score+=3
    if transcipt in RetrievedWords[1]:
        query_score+=2
    if transcipt in RetrievedWords[2]:
        query_score+=1
    
    AvgScore+=query_score
    
    
    








AvgScore/=len(SetOneNames)
#percentager
AvgScore=(AvgScore*100.0)/MaximumScore


with open('/tmp/basebase.txt','w') as arxeio:
    arxeio.write('avg score ' + str(AvgScore ) + '\n')
        
        
