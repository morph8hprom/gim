#!/usr/bin/env python3

import os
import json
import textwrap
import cmd2
from pkg_resources import resource_string
from gim import json_handler as jh
from gim import item

class Command(cmd2.Cmd):
    def __init__(self):
        super().__init__()
        # Set break_long_words to False to prevent words being split
        self.break_long_words = False
        self.prompt = '>'
        # conf_new is a flag for confirming creating of a new file
        self._conf_new = False
        # current working directory
        self._cwd = None
        # extension
        self._ext = None
        # data file for cmd print messages
        self._msgs_file = 'data/cmd_msgs.json'
        # variable to hold instance of MessageHandler()
        self._msgs = None
        # variable to hold instance of jh.DirectoryFiles()
        self._all_files = None
        # variable to hold instance of jh.ItemData()
        self._current_file = None
        # Load all print messages into a dictionary for easy access
        self._load_msgs()
        # Update _all_files
        self._update_dir()
        # Display startup messages
        self._startup()

    def _update_dir(self):
        """
        Create instance of jh.DirectoryFiles() using default parameters
        """

        self._all_files = jh.DirectoryFiles()

    def _load_msgs(self):
        """
        Load cmd messages from json file specified by self._msgs_file
        """

        jsontext = resource_string(__name__, self._msgs_file)
        d = json.loads(jsontext.decode('utf-8'))
        self._msgs = MsgHandler(**d)

    def _startup(self):
        """
        Print startup messages
        """
        self._msgs._print_msg('welcome')
        self._msgs._print_msg('new_or_load')

    def do_new(self, arg):
        """
        If current file is None, create new instance of jh.ItemData using
        parameters from self._all_files to generate a filename.
        If current file is not None ask for confirmation before creating new
        instance
        """
        if self._current_file == None:
            self._cwd = self._all_files._directory
            self._ext = self._all_files._extension
            self._next = self._all_files._next
            _filename = '{}item{}{}'.format(self._cwd, self._next, self._ext)
            self._current_file = jh.ItemData(_filename)
        else:
            self._conf_new = True
            self._msgs._print_msg('current_not_none')

    def do_yes(self, arg):
        
        if self._conf_new == True:
            self._cwd = self._all_files._directory
            self._ext = self._all_files._extension
            _filename = '{}item{}{}'.format(self._cwd, self._next, self._ext)
            print('Now working on new file {}'.format(self._current_file._filename))
            self._current_file = jh.ItemData(_filename)
            self.conf_new = False
        else:
            pass









class MsgHandler():
    def __init__(self, **kwargs):
        self.__dict__.update((key, value) for key, value in kwargs.items())


    def _print_msg(self, msg):
        for line in textwrap.wrap(vars(self)[msg], 80):
            print(line)


def test():
    test_inst = Command()
    test_inst.cmdloop()


if __name__ == "__main__":
    test()
