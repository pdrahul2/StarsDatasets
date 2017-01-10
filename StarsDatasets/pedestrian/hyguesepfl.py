from StarsDatasets import StarsDatasets
import os
import json
import pickle


class hyguesepfl(StarsDatasets):
    annotation_full = []
    peopleCount = 0

    def __init__(self, base_path):
        super(hyguesepfl, self).__init__("EPFL corridor depth", base_path, "*.jpg")
        self.annotation_full = self.read_annotation('annotations.pkl')
        for i in range(0, len(self.annotation_full)):
            self.peopleCount += len(self.annotation_full[i])
        self.populate_dict()

    def populate_dict(self):
        filesPath = os.path.join(self._base_path, "JPEGDepths")
        files_p=[]
        files_np=[]
        i = 0
        i = 0
        for filename in os.listdir(filesPath):
            if '.' in filename:
                if filename[filename.index('.'):] == ".jpg":
                    f_name = filename.split('.')[0] + ".txt"
                    line = os.path.join(self._base_path, 'annotations', f_name)
                    if not self.annotation_full[i]:
                        files_np.append(line)
                    else:
                        files_p.append(line)

                    i += 1

        self._obj_dict['pedestrian'] = files_p
        self._obj_dict['non-pedestrian'] = files_np
        return None

    def read_annotation(self, annotation_file):
        annotations_file_path = os.path.join(self._base_path, "Annotations", annotation_file)
        if not os.path.isfile(annotations_file_path):
            raise ValueError('The annotation file %s does not exist.' % annotations_file_path)
        annotations = pickle.load(open(annotations_file_path))
        return annotations

    def get_data(self, file_list, object_list=None):
        annotation_dict = {}
        fid = open(file_list, 'r')
        for line in fid:
            fname = os.path.splitext(os.path.basename(line))[0] + '.txt'
            fpath = os.path.dirname(os.path.dirname(line))
            line = os.path.join(fpath, 'annotations', fname)
            line_number = int(os.path.splitext(os.path.basename(line))[0])-1
            if line in self._obj_dict['pedestrian']:
                annotation_dict[line] = self.annotation_full[line_number]
        annotations_file_name = os.path.join(os.path.dirname(file_list), "annotations.json")
        with open(annotations_file_name, 'w') as file_name:
            json.dump(annotation_dict, file_name)
        return annotation_dict
