from StarsDatasets.pedestrian import inria
Inria = inria.inria('/home/uujjwal/datasets/pedestrian/INRIAPerson')

print Inria._name
print len(Inria._obj_dict['pedestrian'])
print len(Inria._obj_dict['non-pedestrian'])

annotation_dict = Inria.get_data('/home/uujjwal/datasets/pedestrian/INRIAPerson/Train/pos/filelist.txt')
print annotation_dict
print len(annotation_dict.keys())