#!/usr/bin/env python3

import os
import json
import cmd2
from pkg_resources import resource_string
from gim import json_handler as jh
from gim import item

class Command(cmd2.Cmd):
    def __init__(self):
        super().__init__()
        self.prompt = '>'
        self._msgs_file = 'data/cmd_msgs.json'
        self._msgs = {}
        self._all_files = None
        self._current_file = None
        # Load all print messages into a dictionary for easy access
        self._load_msgs()

    def _load_msgs(self):
        jsontext = resource_string(__name__, self._msgs_file)
        d = json.loads(jsontext.decode('utf-8'))
        self._msgs = d


    def _startup(self):
        pass
