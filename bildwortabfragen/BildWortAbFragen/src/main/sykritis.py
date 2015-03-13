#gia kathe pic sto queries 
#sygkrine ta me to test set
#fyla ta results sto db
import sys,glob,MySQLdb,os,math
from DTWFeature import DTWFeature
from DynamicWarping import EventHorizon

#Column based DTW  DEPRECATEDDDDDDDD

MeinSql = MySQLdb.connect(host="localhost", # your host, usually localhost
                    user="seidman", # your username
                    passwd="seidman@localhost", # your password
                    db="Washington") # name of the data base
        
        
        
        



'''
arg[1] synthetic
arg2 handwritten
arg3 truth file
arg4 threshold of series len percentage 
arg5 band width
'''


SynthFileNames=glob.glob(sys.argv[1]+'*.png1')
HandFileNames=glob.glob(sys.argv[2]+'*.png2')
HandGroundTruth=[]
Thres_Len=float(sys.argv[4])
Band_Width=int(sys.argv[5])

with open('/tmp/DTWStilesParamts.txt','w') as arxeio:
    arxeio.write('thres len ' + sys.argv[4] + '\n')
    arxeio.write('rzoni ' + sys.argv[5] + '\n')
  

#read handwritten truth
with open(sys.argv[3],'r') as file:
    for line in file:
        HandGroundTruth.append(line)


EV=EventHorizon()

print len(HandFileNames)
RealComps=0 # how many comparisons returned a non infinite cost
Infinities=0 #count infinities as well

#Store in memory only the handwritten features
Hand_Series=[]
Truth=[]

#for each handwritten image

for i in xrange(0,len(HandFileNames)):
        print '------------------------------'
        for line in HandGroundTruth:
           
            if os.path.basename(HandFileNames[i].replace('.png','')) in line:
                tmp=line.split(' ')
                
               
                Truth.append(tmp[1])
                #gather the features
                print 'gathering features for ',HandFileNames[i],'=',tmp[1]
                Hand_Series.append(EV.getFeatures(HandFileNames[i]))




Comparisons=len(SynthFileNames)*len(HandFileNames)


#for each synthetic image
for Fake in SynthFileNames:
    print 'gathering features for',Fake
    S=EV.getFeatures(Fake)
    
    
   
  
    #for every handwritten image
    for i in xrange(0,len(HandFileNames)):
             
        
        Comparisons-=1    
        dist=EV.MultiDynTimeWarping(S, Hand_Series[i],Band_Width,Thres_Len) #band width
        
        if math.isinf(dist)==False:
            
            print 'DTW cost',os.path.basename(Fake),'and',os.path.basename(HandFileNames[i]),  Truth[i],dist
            RealComps+=1       
                
            #add result to mysql
            try:
                qr=MeinSql.cursor()
                erotima="Insert INTO Stiles (SynthFile,HandFile,HandWord,Score,Sakoe,Thres) VALUES('"+ os.path.basename(Fake).replace('.png','') +"','"+os.path.basename(HandFileNames[i]) +"','"+ Truth[i]+"','" + str(dist) +"','"+ str(Band_Width)+"','"+ str(Thres_Len)+"')"                       
                print erotima
                #do not insert inf values
                qr.execute(erotima)
                MeinSql.commit()
            
            except Exception as ex:
                with open('/tmp/lathos.txt','w') as arxeio:
                    arxeio.write("fak")
                print ex
            finally:
                print ''

        else:
            Infinities+=1
    with open('/tmp/DTWStiles.txt','w') as arxeio:
        arxeio.write('apomenoun ' + str(Comparisons ) + '\n')
        arxeio.write('real comps ' + str(RealComps) + '\n')
        arxeio.write('apeiro ' + str(Infinities) + '\n')