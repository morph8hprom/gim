#!/usr/bin/env python3

import os
import json
import textwrap
import cmd2
from pkg_resources import resource_string
from gim import json_handler as jh
from gim import item as i

class Command(cmd2.Cmd):
    def __init__(self):
        super().__init__()
        # Set break_long_words to False to prevent words being split
        self.break_long_words = False
        self.prompt = '>'

        # FLAGS
        # flag for confirming creating a new file
        self._conf_new = False
        # flag for selecting item_type
        self._sel_type = False
        # flag for editting attributes
        self._edit_att = False
        # flag for confirming saving a file
        self._conf_save = False

        # current working directory
        self._cwd = None
        # extension
        self._ext = None
        # data file for cmd print messages
        self._msgs_file = 'data/cmd_msgs.json'
        # variable to hold instance of MessageHandler()
        self._msgs = None
        # data file for item attributes
        self._att_file = 'data/item_att.json'
        # variable to hold filename for creation of ItemData() instance
        self._filename = None
        # variable to hold all item attributes dict
        self._all_att = None
        # variable to hold specific item type attributes dict
        self._item_att = None
        # variable to hold string of item attributes for do_attributes method
        self._att_str = None
        # variable to hold instance of jh.DirectoryFiles()
        self._all_files = None
        # variable to hold instance of jh.ItemData()
        self._current_file = None
        # Load all print messages into a dictionary for easy access
        self._load_cmd_msgs()
        # Load item _attributes
        self._load_att()
        # Update _all_files
        self._update_dir()
        # Display startup messages
        self._startup()

    def _update_dir(self):
        """
        Create instance of jh.DirectoryFiles() using default parameters
        """

        self._all_files = jh.DirectoryFiles()

    def _load_cmd_msgs(self):
        """
        Load cmd messages from json file specified by self._msgs_file
        """

        jsontext = resource_string(__name__, self._msgs_file)
        d = json.loads(jsontext.decode('utf-8'))
        self._msgs = MsgHandler(**d)

    def _load_att(self):
        """
        Load item attribute dictionary from json file specified by self._att_file
        """

        jsontext = resource_string(__name__, self._att_file)
        d = json.loads(jsontext.decode('utf-8'))
        self._all_att = d

    def _save_file(self):
        self._current_file._to_json()
        with open(self._current_file._filename, 'w') as f:
            f.write(self._current_file._json_dump)

    def _edit_att(self, att, val):
        """
        Used to set attribute provided to value provided
        """
        self._current_file[att] = val



    def _startup(self):
        """
        Print startup messages
        """
        self._msgs._print_msg('welcome')
        self._msgs._print_msg('new_or_load')

    def _create_new(self):
        """
        Used to create a new instance of jh.ItemData()
        and change the _sel_type flag to True
        """
        self._cwd = self._all_files._directory
        self._ext = self._all_files._extension
        self._next = self._all_files._next
        filename = '{}item{}{}'.format(self._cwd, self._next, self._ext)
        self._current_file = jh.ItemData(None, filename)
        self._sel_type = True
        self._msgs._print_msg('select_type')


    def _select_type(self, type):
        self._current_file._item_type = type
        self._current_file['item_type'] = type
        self._item_att = self._all_att[type]
        self._att_str = ', '.join(self._item_att)

    def do_new(self, arg):
        """
        If current file is None, create new instance of jh.ItemData using
        parameters from self._all_files to generate a filename.
        If current file is not None ask for confirmation before creating new
        instance
        """
        if self._current_file == None:
            self._create_new()

        else:
            self._conf_new = True
            self._msgs._print_msg('current_not_none')

    def do_save(self,arg):
        if self._current_file == None:
            pass
        else:
            self._conf_save = True
            self._msgs._print_msg('save_msg')


    def do_yes(self, arg):
        if self._conf_new:
            self._create_new()
            self._conf_new = False

        elif self._conf_save:
            self._save_file()
            self._conf_save = False

        else:
            pass

    def do_no(self, arg):
        if self._conf_new:
            self._conf_new = False
        elif self._conf_save:
            self._conf_save = False
        else:
            pass


    def do_weapon(self, arg):
        """
        Set item type to Weapon when creating a new item.
        """
        if self._sel_type:
            self._select_type('Weapon')
            self._sel_type = False
            self._edit_att = True
            self._msgs._print_msg('att_msg')
        else:
            pass


    def do_armor(self, arg):
        """
        Set item type to Armor when creating a new item.
        """
        if self._sel_type:
            self._select_type('Armor')
            self._sel_type = False
            self._edit_att = True
            self._msgs._print_msg('att_msg')
        else:
            pass


    def do_consumable(self, arg):
        """
        Set item type to Consumable when creating a new item.
        """
        if self._sel_type:
            self._select_type('Consumable')
            self._sel_type = False
            self._edit_att = True
            self._msgs._print_msg('att_msg')
        else:
            pass


    def do_show(self, arg):
        print(self._current_file._dict)


    def do_edit(self, arg):
        if arg in self._item_att:
            self._msgs._print_msg(arg)
            val = input('>')
            self._current_file[arg] = val

        else:
            self._msgs._print_msg('invalid_att')


    def do_attributes(self, arg):
        self._msgs._print_msg('current_attributes')
        print(self._att_str)



class MsgHandler():
    def __init__(self, **kwargs):
        self.__dict__.update((key, value) for key, value in kwargs.items())


    def _print_msg(self, msg):
        for line in textwrap.wrap(vars(self)[msg], 80):
            print(line)


def test():
    test_inst = Command()
    #test_inst.cmdloop()
    print(test_inst._all_files._files)


if __name__ == "__main__":
    test()
