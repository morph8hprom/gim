#!/usr/bin/env python3

import json


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


    def to_json(self):
        self._json_dump = json.dumps(self._dict)
