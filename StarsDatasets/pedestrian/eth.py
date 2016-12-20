from StarsDatasets import StarsDatasets
import os
import re
import fnmatch


class eth(StarsDatasets):
    def __init__(self, base_path):
        super(eth, self).__init__("ETH Pedestrian", base_path, "*.png")
        self._annotations = {}
        self.populate_dict()


    def populate_dict(self):
        idlfiles = []
        for root, dirnames, filenames in os.walk(self._base_path):
            for filename in fnmatch.filter(filenames, '*.idl'):
                idlfiles.append(os.path.join(root, filename))

        noann_regex = re.compile('"(.+)"[;.]')
        name_regex = re.compile('"(.+)":')
        eth_regex = re.compile('(\d+),\s+(\d+),\s+(\d+),\s+(\d+)')

        self._obj_dict['pedestrian'] = []
        self._obj_dict['non-pedestrian'] = []
        for idl in idlfiles:
            fid = open(idl, 'r')
            idlpath = os.path.dirname(idl)
            for line in fid:
                line = line.strip()
                if re.match(noann_regex, line):
                    name = map(str, re.findall(noann_regex, line))[0]
                    name = os.path.basename(name)
                    if not name.endswith('_0.png'):
                        name = os.path.splitext(name)[0] + '_0.png'

                    fname = os.path.join(idlpath, name)
                    self._obj_dict['non-pedestrian'].append(fname)
                else:
                    name = map(str, re.findall(name_regex, line))[0]
                    name = os.path.basename(name)
                    if not name.endswith('_0.png'):
                        name = os.path.splitext(name)[0] + '_0.png'
                    fname = os.path.join(idlpath, name)
                    annotations = re.findall(eth_regex, line)
                    annotations = map(lambda x: tuple(map(int, list(x))), annotations)
                    self._annotations[fname] = annotations
                    self._obj_dict['pedestrian'].append(fname)
        return None

    def get_data(self, file_list, object_list=None):
        annotations = {}
        fid = open(file_list, 'r')
        print('For ETH Zurich any file for which annotations are not available will not be processed. No error will'
              'be displayed.')
        for line in fid:
            line = line.strip()
            if line in self._obj_dict['pedestrian']:
                annotations[line] = self._annotations[line]
        return annotations

    def read_annotation(self, annotation_file):
        return NotImplemented
