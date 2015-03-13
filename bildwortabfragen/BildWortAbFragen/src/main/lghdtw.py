import MySQLdb,sys,csv,os.path,math,mlpy

#from main.DynamicWarping import EventHorizon

'''
Dynamic Time Warping using Local Gradient Histogram Features and mlpy


maybe non overlapping windows
---------------------------------------------
inputs
 synth image file names 
 synth feats
 hand image file names 
 hand feats 
 truth file
 Band Width
 Band Type 
---------------------------------------------

output to mysql
'''


#store in memory
#for every synthetic image
#read  its features
#do the same for each handwritten


Vergleichen=0 #actual comparisons...

MeinSql = MySQLdb.connect(host="localhost", # your host, usually localhost
                    user="seidman", # your username
                    passwd="seidman@localhost", # your password
                    db="Washington") # name of the data base
        
        
        
SynthFileNames=[]
SynthGroundTruth=[]
SynthFeats=[]

HandFileNames=[]
HandGroundTruth=[]
HandFeats=[]
AllHandFeats=[]

SynthNamesCsv=sys.argv[1] #file names and feat ranges
SynthFeatsCsv=sys.argv[2]

HandNamesCsv=sys.argv[3]
HandFeatsCsv=sys.argv[4]
HandTruthFile=sys.argv[5]
band_width=int(sys.argv[6]) #band width
ZoneType=sys.argv[7] #SC or ITK

Infinities=0

#read synthetic features
with open (SynthFeatsCsv,'rb') as file:
    csvreader=csv.reader(file,delimiter=',')
    for row in csvreader:
        SynthFeats.append(row)
        
        


#read synthetic image filenames
with open (SynthNamesCsv,'rb') as file:
    csvreader=csv.reader(file,delimiter=',')
    for row in csvreader:
        SynthFileNames.append(row)
        




#read handwritten image filenames
with open (HandNamesCsv,'rb') as file:
    csvreader=csv.reader(file,delimiter=',')
    for row in csvreader:
        print row
        HandFileNames.append(row)


        
                
#read handwritten features
with open (HandFeatsCsv,'rb') as file:
    csvreader=csv.reader(file,delimiter=',')
    for row in csvreader:
        HandFeats.append(row)
        



        


#read handwritten image features


for Real in HandFileNames:
    print 'gathering features for ',Real[0],'ranging from',Real[1],'to',Real[2]
    R=[]
    for i in xrange(int(Real[1]),int(Real[2])):
        #print 'getting vector',i
        
        for v in HandFeats[i]:
            R.append(float(v))
    AllHandFeats.append(R)
            


#read handwritten truth
with open(HandTruthFile,'r') as file:
    for line in file:
        HandGroundTruth.append(line)




RealComps=0
Comparisons=len(SynthFileNames)*len(HandFileNames)

#begin DTW
for Fake in SynthFileNames:
    
    print 'gathering features for ',Fake[0],'ranging from',Fake[1],'to',Fake[2]
    S=[]
    for i in xrange(int(Fake[1]),int(Fake[2])):
        #print 'getting vector',i
        
        for v in SynthFeats[i]:
            S.append(float(v))
            
    #for every row of hand images and feats
    for i in xrange(0,len(HandFileNames)):
        #write to a file the actual len of the series
        transcript=''
        for line in HandGroundTruth:
            #print line
            if os.path.basename(HandFileNames[i][0]).replace('.png','') in line:
                tmp=line.split(' ')
                #print tmp[0],tmp[1]
                transcript=tmp[1].replace('\n','')
                    
        print '---------------------------------------------'
        
        #https://github.com/sauliusl/mlpy/blob/master/mlpy/dtw/dtw.pyx
        #dont compare if the dont have a 75 differece
        if len(AllHandFeats[i])>len(S) and len(S)/float(len(AllHandFeats[i]))<0.65: 
            # print 'skip'
            dist=float("inf")
        elif len(S)>len(AllHandFeats[i]) and len(AllHandFeats[i])/float(len(S))<0.65:
            # print 'skip'
            dist=float("inf")
        else:
            
            #my DTW 
            #EV=EventHorizon()
            #dis=EV.SimpleDynTimeWarp(S, AllHandFeats[i], band_width)
            
            
            if 'SC' in ZoneType:
                dist,cost,path=mlpy.dtw_std(S,AllHandFeats[i], dist_only=False, metric='euclidean', constraint='slanted_band', k=band_width)
            else:
                dist,cost,path=mlpy.dtw_std(S,AllHandFeats[i], dist_only=False, metric='euclidean', constraint='itakura', k=band_width)
                
            dist/=float(len(S)+len(AllHandFeats[i]))
                
            print 'DTW :',os.path.basename(Fake[0]),transcript,'=',dist
    
            if math.isinf(dist)==False:
                
                RealComps+=1  
                #add result to mysql
                try:
                    qr=MeinSql.cursor()
    
                    erotima="Insert INTO Local (SynthFile,HandFile,HandWord,Score,Zoni,Platos) VALUES('"+ os.path.basename(Fake[0])+"','"+os.path.basename(HandFileNames[i][0]) +"','"+ transcript+"','" + str(dist)+"','"+ ZoneType+"','"+ str(band_width) +"')"
                    #print erotima
                    #do not insert inf values
                    qr.execute(erotima)
                    MeinSql.commit()
                
                except Exception as ex:
                    print 'error writing results to db'
                    with open('/tmp/lgh_lathos.txt','w') as arxeio:
                        arxeio.write("fak")
                    print ex
                    sys.exc_clear()
                    Comparisons+=1
                finally:
                    print ''
            else:
                Infinities+=1
        #write in the file the remaining comparisons
        Comparisons-=len(HandFileNames)
        
        with open('/tmp/DTWLGH.txt','w') as arxeio:
            arxeio.write('apomenoun ' + str(Comparisons ) + '\n')
            arxeio.write('real comps ' + str(RealComps) + '\n')
            arxeio.write('apeiro ' + str(Infinities) + '\n')
            arxeio.write('platos zonis ' + str(band_width) + '\n')
            arxeio.write('zoni ' + ZoneType + '\n')


