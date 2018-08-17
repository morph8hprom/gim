#!/usr/bin/env python3

import json
import glob

class DirectoryFiles():
    def __init__(self, directory = 'data/', filename = '*' extension = '.json'):
        self._directory = directory
        self._filename = filename
        self._extension = extension
        self._files = None
        self._digits = []
        self._next = None
        # Build a list of all files in the data directory
        self._update_files()
        # Isolate only the digits in the filenames
        self._isolate_digits()
        # Store digit for next file in self._next
        self._get_next()

    def _update_files(self):
        self._files = glob.glob('{}{}{}'.format(self._directory, self._filename, self._extension))
        self._files.sort()

    def _isolate_digits(self):
        for filename in self._files:
            digit = ''
            for c in filename:
                if c.isdigit():
                    digit += c
            self._digits.append(int(digit))    

    def _get_next(self):
        self._next = str(self._digits[-1] + 1)



class JsonHandler():
    def __init__(self, data):
        self._data = data

    def _save_file(self):
        with open(self._data._filename, 'w') as f:
            f.write(self._data._json_dump)


class ItemData():
    def __init__(self):
        self._dict = {}
        self._filename = None
        self._json_dump = None
        self._to_json()

    def _to_json(self):
        self._json_dump = json.dumps(self._dict)
