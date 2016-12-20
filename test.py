from StarsDatasets.pedestrian import inria, eth, tudbrussels
Inria = inria.inria('/home/uujjwal/datasets/pedestrian/INRIAPerson')

print Inria._name
print len(Inria._obj_dict['pedestrian'])
print len(Inria._obj_dict['non-pedestrian'])

annotation_dict = Inria.get_data('/home/uujjwal/datasets/pedestrian/INRIAPerson/Train/pos/filelist.txt')
print annotation_dict
print len(annotation_dict.keys())

ETH = eth.eth('/home/uujjwal/datasets/pedestrian/ETHZ')
annotation_dict = ETH.get_data('/home/uujjwal/datasets/pedestrian/ETHZ/seq04/filelist.txt')
print annotation_dict
print ETH._obj_dict['pedestrian']

TUD = tudbrussels.tudbrussels('/home/uujjwal/datasets/pedestrian/Brussels')
print len(TUD._obj_dict['non-pedestrian'])
annotation_dict = TUD.get_data('/home/uujjwal/datasets/pedestrian/Brussels/TUD-MotionPairs/positive/filelist.txt')
print annotation_dict