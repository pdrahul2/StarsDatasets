from StarsDatasets import StarsDatasets
from PIL import Image
import os
import json


class peta(StarsDatasets):
    def __init__(self, base_path):
        super(peta, self).__init__("PETA Dataset", base_path, "multiple")
        self.populate_dict()

    def populate_dict(self):
        imgfiles = []
        for root, dirnames, filenames in os.walk(self._base_path):
            for filename in filenames:
                if filename.endswith(('.jpg', '.png', '.bmp')):
                    imgfiles.append(os.path.join(root, filename))
        self._obj_dict['pedestrian'] = imgfiles
        return None

    def read_annotation(self, annotation_file):
        return NotImplemented

    def get_data(self, file_list, object_list=None):
        fid = open(file_list, 'r')
        annotations = {}
        annotations['pedestrian'] = []
        for line in fid:
            line = line.strip()
            if line in self._obj_dict['pedestrian']:
                img = Image.open(line, 'r')
                sz = list(img.size)
                sz = [0, 0] + map(lambda x: x - 1, sz)
                annotations[line] = sz

        annotations_file_name = os.path.join(os.path.dirname(file_list), "annotations.json")
        with open(annotations_file_name, 'w') as file_name:
            json.dump(annotations, file_name)
        return annotations
