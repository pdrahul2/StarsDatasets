from StarsDatasets.pedestrian import inria, eth, tudbrussels, caltech
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
"""
PETA = peta.peta('/Users/meetukme/Downloads/PETA')

annotation_dict = PETA.get_data('/Users/meetukme/Downloads/PETA/filelist.txt')

print PETA._obj_dict
print annotation_dict

"""

cal = caltech.caltech('/home/uujjwal/datasets/pedestrian/caltech/images')

print len(cal._obj_dict['pedestrian'])
print len(cal._obj_dict['non-pedestrian'])
print len(cal._annotations)

annotation_dict = cal.get_data('/home/uujjwal/datasets/pedestrian/caltech/images/images/set02/filelist.txt')
print len(annotation_dict)
print annotation_dict