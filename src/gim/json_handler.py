#!/usr/bin/env python3

import json
import glob
from pkg_resources import resource_string

class DirectoryFiles():
    def __init__(self, directory = 'data/', filename = '*', extension = '.json'):
        self._directory = directory
        self._filename = filename
        self._extension = extension
        self._full_path = "{}{}{}".format(self._directory, self._filename, self._extension)
        self._files = None
        self._digits = []
        self._next = None
        # Build a list of all files in the data directory
        self._update_files()
        # Isolate only the digits in the filenames
        self._isolate_digits()
        # Store digit for next file in self._next
        self._get_next()

    def __repr__(self):
        return "{}\n{}\n{}".format(self.__class__.__name__, self._full_path, self._files)

    def _update_files(self):
        self._files = glob.glob('{}'.format(self._full_path))
        self._files.sort()

    def _isolate_digits(self):
        for filename in self._files:
            digit = ''
            for c in filename:
                if c.isdigit():
                    digit += c
            try:
                self._digits.append(int(digit))
            except ValueError:
                pass

    def _get_next(self):
        self._next = str(self._digits[-1] + 1)


class ItemData():
    def __init__(self, item_type = None, filename = None):
        self._item_type = item_type
        self._filename = filename
        self._attributes = None
        self._dict = {}
        self._json_dump = None
        self._mangle_file = 'data/mangle.json'
        self._mangle_dict = None
        self._update_mangle()

    def __iter__(self):
        return iter(self._dict.items())

    def __setitem__(self, key, item):
        self._dict[key] = item

    def _update_mangle(self):
        jsontext = resource_string(__name__, self._mangle_file)
        d = json.loads(jsontext.decode('utf-8'))
        self._mangle_dict = d


    def _mangle_names(self):
        """
        Used to mangle attribute names to ensure that there are no conflicts
        when creating an instance of Item() class.
        """
        for k, v in self._mangle_dict.items():
            try:
                self._dict[v] = self._dict.pop(k)
            except (KeyError, ValueError):
                pass



    def _to_json(self):
        self._json_dump = json.dumps(self._dict)

def test():
    test = DirectoryFiles()

if __name__ == "__main__":
    test()
