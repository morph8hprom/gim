#!/usr/bin/env python3

from pkg_resources import resource_string
from gim import item
import json

"""
File used to define ItemDict class and it's methods
"""

class ItemDict():
    def __init__(self, id = 1, num_of_items = 2):
        # Dictionary containing reference to all items
        self.all_items = {}
        # Dictionary containing reference to only weapons
        self.weapons = {}
        # Dictionary containing reference to only armor
        self.armor = {}
        # Dictionary containing reference to only consumables
        self.consumables = {}

        self._id = id
        self._num_of_items = num_of_items
        self._update_all_items()
        self._update_weapons()
        self._update_armor()
        self._update_consumables()

    def __iter__(self):
        return iter(self.all_items.items())

    def __len__(self):
        return len(self.all_items)

    def __contains__(self, item):
        return item.id in self.all_items

    def __getitem__(self, item):
        return self.all_items[item.id]

    def _build_item(self, id):
        """
        Gathers item data from json file and returns instance object based on
        item type.
        """
        jsontext = resource_string(__name__, 'data/item{}.json'.format(id))
        d = json.loads(jsontext.decode('utf-8'))
        d['id'] = id
        if d['item_type'] == 'Weapon':
            item = Weapon(**d)
        elif d['item_type'] == 'Armor':
            item = Armor(**d)
        elif d['item_type'] == 'Consumable':
            item = Consumable(**d)
        return item

    def _update_main_dict(self):
        d = {}
        for i in range(self._id, self._num_of_chars):
            try:
                d[i] = self._build_character(i)
            except FileNotFoundError:
                print('File not found.  Please check to make sure it exists')

        self.all_chars = d

    def _update_weapons(self):
        d = {}
        for i in self.all_items.values():
            if i.item_type == 'Weapon':
            d[i.id] = i
        self.weapons = d

    def _update_armor(self):
        d = {}
        for i in self.all_items.values():
            if i.item_type == 'Armor'
            d[i.id] = i
        self.armor = d
