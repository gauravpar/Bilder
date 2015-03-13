#gia kathe pic sto queries 
#sygkrine ta me to test set
#fyla ta results sto db
#use mlpy.DTW
import sys,MySQLdb,math,pickle
import mlpy


#Column based DTW top profile only

MeinSql = MySQLdb.connect(host="localhost", # your host, usually localhost
                    user="seidman", # your username
                    passwd="seidman@localhost", # your password
                    db="Washington") # name of the data base
        
        
        
        



'''
arg[1] synthetic names txt pickle
arg[2] synthetic feats txt pickle
arg[3] handwritten names txt pickle
arg[4] handwritten feats txt pickle
arg[5] truth file
arg[6] band width
arg[7] SC ITK
'''

SynthNamesFile=sys.argv[1]
SynthFeatsFile=sys.argv[2]

HandNamesFile=sys.argv[3]
HandFeatsFile=sys.argv[4]

TruthFile=sys.argv[5]

PlatosZonis=int(sys.argv[6])
Zoni=sys.argv[7]

#unpickle   4 favorite_color = pickle.load( open( "save.p", "rb" ) )
Hand_Names=pickle.load(open(HandNamesFile,'rb'))
Hand_Series=pickle.load(open(HandFeatsFile,'rb'))

SynthNames=pickle.load(open(SynthNamesFile,'rb'))
SynthSeries=pickle.load(open(SynthFeatsFile,'rb'))



HandGroundTruth=[]
 

#read handwritten truth
with open(TruthFile,'r') as file:
    for line in file:
        HandGroundTruth.append(line)



RealComps=0 # how many comparisons returned a non infinite cost
Infinities=0 #count infinities as well
Comparisons=len(SynthNames)*len(Hand_Names)

#memory...

#for each synthetic image
for pseudo in xrange(0,len(SynthNames)):
    
    
    with open('/tmp/DTWStiles.txt','w') as arxeio:
        arxeio.write('apomenoun ' + str(Comparisons ) + '\n')
        arxeio.write('real comps ' + str(RealComps) + '\n')
        arxeio.write('apeiro ' + str(Infinities) + '\n')
        arxeio.write('platos zonis ' + str(PlatosZonis) + '\n')
        arxeio.write('zoni ' + Zoni + '\n')
        
    transcipt=''
    #for every handwritten image
    for real in xrange(0,len(Hand_Names)):
             
        print '------------------------------'
        for line in HandGroundTruth:
           
            if Hand_Names[real].replace('.png','') in line:
                tmp=line.split(' ')
                
                
                transcipt=tmp[1]
                
        Comparisons-=1    
        
        # parameter descriptions
        #https://github.com/sauliusl/mlpy/blob/master/mlpy/dtw/dtw.pyx
        #dont compare if the dont have a 75 differece
        if len(Hand_Series[real])>len(SynthSeries[pseudo]) and len(SynthSeries[pseudo])/float(len(Hand_Series[real]))<0.65: 
            # print 'skip'
            dist=float("inf")
        elif len(SynthSeries[pseudo])>len(Hand_Series[real]) and len(Hand_Series[real])/float(len(SynthSeries[pseudo]))<0.65:
            # print 'skip'
            dist=float("inf")
        else:
            try:
                if 'SC' in Zoni:
                    dist,cost,path=mlpy.dtw_std(SynthSeries[pseudo],Hand_Series[real], dist_only=False, metric='sqeuclidean', constraint='sakoe_chiba', k=PlatosZonis)
                else:
                    dist,cost,path=mlpy.dtw_std(SynthSeries[pseudo],Hand_Series[real], dist_only=False, metric='euclidean', constraint='slanted-band', k=PlatosZonis)
            except Exception as ex:
                sys.exc_clear()  
                with open('/tmp/col_lathos.txt','w') as arxeio:
                            arxeio.write("dtw fak")  
            finally:
                
                dist=dist/float(len(SynthSeries[pseudo]) + len(Hand_Series[real]))
                print 'Normalized cost',dist
                
                
                print 'DTW cost',SynthNames[pseudo],'and',Hand_Names[real],  transcipt,dist
        
                
                if math.isinf(dist)==False:
                    
                    RealComps+=1       
                        
                    #add result to mysql
                    try:
                        qr=MeinSql.cursor()
                        erotima="Insert INTO Stiles (SynthFile,HandFile,HandWord,Score,Zoni,Platos) VALUES('"+ SynthNames[pseudo].replace('.png','') +"','"+Hand_Names[real] +"','"+ transcipt +"','" + str(dist) +"','"+ Zoni+"','"+ str(PlatosZonis) +"')"                       
                        print erotima
                        #do not insert inf values
                        qr.execute(erotima)
                        MeinSql.commit()
                    
                    except Exception as ex:
                        with open('/tmp/col_lathos.txt','w') as arxeio:
                            arxeio.write("fak")
                        print ex
                        sys.exc_clear()
                    finally:
                        print ''
        
                else:
                    Infinities+=1

