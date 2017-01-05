from StarsDatasets.pedestrian import inria, eth, tudbrussels, caltech, people

People = people.people('/run/netsop/u/sop-nas2a/vol/home_stars/rpandey/inria/dataset/mensa_seq0_1.1/')
print People._name
print len(People._obj_dict['pedestrian'])
print len(People._obj_dict['non-pedestrian'])

annotation_dict = People.get_data('/run/netsop/u/sop-nas2a/vol/home_stars/rpandey/inria/dataset/filelist.txt')
# print annotation_dict
print len(annotation_dict.keys())
