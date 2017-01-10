from StarsDatasets import StarsDatasets
import glob
import os
import re
import json


class inria(StarsDatasets):
    def __init__(self, base_path):
        super(inria, self).__init__("Inria Pedestrian", base_path, "*.png")
        self.populate_dict()
        self._inria_regex = re.compile('\((\d+),\s+(\d+)\)\s+\-\s+\((\d+),\s+(\d+)\)')

    def populate_dict(self):
        files = glob.glob(os.path.join(self._base_path, 'Train', 'pos', self._extension))
        self._obj_dict['pedestrian'] = files
        files = glob.glob(os.path.join(self._base_path, 'Train', 'neg', self._extension))
        self._obj_dict['non-pedestrian'] = files
        files = glob.glob(os.path.join(self._base_path, 'Test', 'pos', self._extension))
        self._obj_dict['pedestrian'] += files
        files = glob.glob(os.path.join(self._base_path, 'Test', 'neg', self._extension))
        self._obj_dict['non-pedestrian'] += files
        return None

    def read_annotation(self, annotation_file):
        """ Reads an annotation file in INRIA pedestrian dataset.
        Each bounding box is returned as (Xmin, Ymin, Xmax, Ymax)"""
        if not os.path.isfile(annotation_file):
            raise ValueError('The annotation file %s does not exist.' % annotation_file)
        fstr = open(annotation_file, 'r').read()
        return re.findall(self._inria_regex, fstr)

    def get_data(self, file_list, object_list=None):
        annotation_dict = {}
        fid = open(file_list, 'r')
        for line in fid:
            fname = os.path.splitext(os.path.basename(line))[0] + '.txt'
            fpath = os.path.dirname(os.path.dirname(line))
            line = os.path.join(fpath, 'annotations', fname)
            annotation_dict[line] = {}
            annotations = self.read_annotation(line)
            annotations = map(lambda x: tuple(map(int, list(x))), annotations)
            annotation_dict[line]['pedestrian'] = annotations

        annotations_file_name = os.path.join(os.path.dirname(file_list), "annotations.json")
        with open(annotations_file_name, 'w') as file_name:
            json.dump(annotation_dict, file_name)
        return annotation_dict
