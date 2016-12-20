import abc
import re


class StarsDatasets(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, name, base_path, extension):
        extpattern = re.compile('^\*\.\w+')
        if extension is not "multiple":
            if not extpattern.match(extension):
                raise ValueError('Extension provided is not valid. It must be of the form *.jpg etc.')
        self._name = name
        self._base_path = base_path
        self._extension = extension
        self._obj_dict = {}

    def get_classes(self):
        """Returns the list of classes in the dataset."""
        return self._obj_dict.keys()

    def ispresent(self, object_type):
        """Returns True of object_type is in the dataset, otherwise False"""
        if object_type in self._obj_dict:
            return True
        else:
            return False

    def num_images(self, object_type=None):
        """If object_type is None, returns a dictionary consisting of all object
         categories and corresponding number of images. If object_type is not in the dataset,
         returns a ValueError. If object_type is present in the dataset, returns the number of images
         of that object_type in the dataset.
         """
        if object_type is None:
            return self._obj_dict

        if self.ispresent(object_type):
            return self._obj_dict[object_type]
        else:
            raise ValueError('%s does not occour in the dataset.' % object_type)

    @abc.abstractmethod
    def read_annotation(self, annotation_file):
        """ Reads a groundtruth file of the dataset and returns the annotations in a dictionary
        """
        return

    @abc.abstractmethod
    def populate_dict(self):
        """Populates obj_dict which is a dictionary with all the object categories in the dataset
        as keys and files corresponding to each category as the corresponding values
        """
        return

    @abc.abstractmethod
    def get_data(self, file_list, object_list=None):
        """Returns the bounding box annotations for the objects in the list of files passed to the functions.
        The annotations are returned in the form of a dictionary.
        object_list is a list of object categories which need to be present in the final dictionary. If object_list
        contains 'others' then all object categories not in the object_list are clumped together into a single key
        called 'others' """
        return
