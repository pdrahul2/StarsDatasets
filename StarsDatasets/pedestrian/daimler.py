from StarsDatasets import StarsDatasets
import os
import re


class daimler(StarsDatasets):
    def __init__(self, base_path):
        super(daimler, self).__init__("Daimler pedestrian detection", base_path, "*.pgm")
        self._annotations = {}

    def populate_dict(self):
        # TODO Intoduce the functionality of storing subcategories of pedestrians in the _obj_dict
        frame_regex = re.compile(';\n([^;]+)')
        name_regex = re.compile('(.+)\.pgm]')
        ispresent_regex = re.compile('#\s\d+')
        annotation_regex = re.compile('\n(\d+)[ ](\d+)[ ](\d+)[ ](\d+)\n')
        gtpath = os.path.join(self._base_path, 'DaimlerBenchmark', 'GroundTruth')
        gtfile = open(os.path.join(gtpath, 'GroundTruth2D.db'), 'r').read()
        frames = re.findall(frame_regex, gtfile)
        self._obj_dict['pedestrian'] = []
        self._obj_dict['non-pedestrian'] = []
        for frame in frames:
            fname = re.findall(name_regex, frame)[0]
            if not re.match(ispresent_regex, frame):
                self._obj_dict['non-pedestrian'].append(fname)
            else:
                self._obj_dict['pedestrian'].append(fname)
                bbox = re.findall(annotation_regex, frame)
                bbox = map(lambda x: tuple(map(int, list(x))), bbox)
                self._annotations[fname] = bbox
        return None

    def read_annotation(self, annotation_file):
        return NotImplemented

    def get_data(self, file_list, object_list=None):
        # TODO introduce the functionality of managing subcategories of pedestrians in daimler dataset

        fid = open(file_list, 'r')
        annotations = {}
        for line in fid:
            fname = os.path.basename(line)
            if fname in self._annotations:
                annotations[line] = self._annotations[fname]
        return annotations
