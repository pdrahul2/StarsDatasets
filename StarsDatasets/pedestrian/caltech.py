from StarsDatasets import StarsDatasets
import os
import re
import fnmatch


class caltech(StarsDatasets):
    def __init__(self, base_path):
        super(caltech, self).__init__("caltech pedestrian", base_path, "*.jpg")
        self.populate_dict()

    def populate_dict(self):
        anndir = os.path.join(self._base_path, 'annotations')
        gtfiles = []
        for root, dirnames, filenames in os.walk(anndir):
            for filename in fnmatch.filter(filenames, '*.txt'):
                gtfiles.append(os.path.join(root, filename))

        self._obj_dict['pedestrian'] = []
        self._obj_dict['non-pedestrian'] = []
        ppl_regex = re.compile('person\s(.+)')
        self._annotations = {}
        for annotation_file in gtfiles:
            gtname = os.path.basename(annotation_file)
            gtpath = os.path.dirname(annotation_file)
            subset = os.path.basename(gtpath)
            setname = os.path.basename(os.path.dirname(gtpath))
            imgpath = os.path.join(self._base_path, 'images', setname, subset)
            imgname = os.path.splitext(gtname)[0] + '.jpg'
            gtfile = open(annotation_file, 'r').read()
            persons = re.findall(ppl_regex, gtfile)
            if len(persons) == 0:
                self._obj_dict['non-pedestrian'].append(os.path.join(imgpath, imgname))
                continue
            self._obj_dict['pedestrian'].append(os.path.join(imgpath, imgname))
            annotation = []
            for person in persons:
                gt = map(int, person.split(' '))
                xmin = gt[5]
                xmax = gt[5] + gt[7]
                ymin = gt[6]
                ymax = gt[6] + gt[8]
                gt = tuple([xmin, xmax, ymin, ymax])
                annotation.append(gt)
            self._annotations[os.path.join(imgpath, imgname)] = annotation
        return None

    def read_annotation(self, annotation_file):
        return NotImplemented

    def get_data(self, file_list, object_list=None):
        fid = open(file_list, 'r')
        print('For caltech pedestrian any file for which annotations are not available will not be processed. No error will'
              'be displayed.')
        annotation_dict = {}
        for line in fid:
            line = line.strip()
            if line in self._annotations:
                annotation_dict[line] = self._annotations[line]
        return annotation_dict




