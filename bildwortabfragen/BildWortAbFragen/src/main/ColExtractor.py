
#read a folder of images
#save top profile to a txt file
import os,glob,sys,pickle
from DynamicWarping import EventHorizon

EV=EventHorizon()
       
Images=[]
Feats=[]        

ImageSet=glob.glob(sys.argv[1]+'*.png')

for img in ImageSet:
    print 'extracting from ',img
    series=EV.getSingleFeature(img)
    #print 'inserting ',os.path.basename(img),'in database'
    Images.append(os.path.basename(img))
    Feats.append(series)


pickle.dump( Images, open( sys.argv[2], "wb" ) )
pickle.dump( Feats, open( sys.argv[3], "wb" ) )


