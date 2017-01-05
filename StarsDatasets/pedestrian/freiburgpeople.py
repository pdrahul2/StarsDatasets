from StarsDatasets import StarsDatasets
import glob
import os
import re


class freiburgpeople(StarsDatasets):
    ORIGINAL_PREFIX="seq"
    annotation_full={}
    peopleCount=0
    def __init__(self, base_path):
        super(freiburgpeople, self).__init__("People depth", base_path, "*.pgm")
        annotation_file=self.read_annotation('track_annotations')
        numPeople=0
        for filename in os.listdir(annotation_file):
            count=0

            fileTrack=os.path.join(annotation_file,filename)
            for line in open(fileTrack):
                numPeople=numPeople+1
                line = line.strip()
                fields = str(line).split(' ')
                if count==0:
                    numPeople=numPeople-1
                    count=1
                    continue
                imgName=fields[0]
                for i in [2,3,4,5]:
                    if int(fields[i])<0:
                        fields[i]=0
                imgName=imgName+".txt"
                fname_d=os.path.join(self._base_path,'annotations',imgName)
                fields = map(lambda x: int(x), fields[2:6])
                fields[2]+=fields[0]
                fields[3]+=fields[1]
                if fname_d not in self.annotation_full.keys():
                    self.annotation_full[fname_d]=[]
                self.annotation_full[fname_d].append(tuple(fields))
        self.peopleCount=numPeople
        self.populate_dict()

    def populate_dict(self):
        filesPath = os.path.join(self._base_path, "depthRecovered1")
        files_p=[]
        files_np=[]
        for filename in os.listdir(filesPath):
            if '.' in filename:
                if filename[filename.index('.'):]==".pgm":
                    if filename[0:len(self.ORIGINAL_PREFIX)]==self.ORIGINAL_PREFIX:
                        fname=filename.split('.')[0]+".txt"
                        line = os.path.join(self._base_path, 'annotations', fname)
                        if line not in self.annotation_full.keys():
                            files_np.append(line)
                        else:
                            files_p.append(line)
        self._obj_dict['pedestrian']=files_p
        self._obj_dict['non-pedestrian']=files_np
        return None

    def read_annotation(self, annotation_file):
        annotationsFilePath=os.path.join(self._base_path, annotation_file)
        if not os.path.isdir(annotationsFilePath):
            raise ValueError('The annotation dir %s does not exist.' % annotationsFilePath)
        return annotationsFilePath

    def get_data(self, file_list, object_list=None):
        annotation_dict = {}
        fid = open(file_list, 'r')
        annotation_file=self.read_annotation('track_annotations')
        for line in fid:
            fname = os.path.splitext(os.path.basename(line))[0] + '.txt'
            if fname[0:len(self.ORIGINAL_PREFIX)]!=self.ORIGINAL_PREFIX:
                raise ValueError('The file name is not appropriate according to the dataset %s', fname)
            fpath = os.path.dirname(os.path.dirname(line))
            line = os.path.join(fpath, 'annotations', fname)
            if line in self._obj_dict['pedestrian']:
                annotation_dict[line] = self.annotation_full[line]
        return annotation_dict
