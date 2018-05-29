#!/usr/bin/env python3

from pkg_resources import resource_string
from gim import item as I
import json

"""
File used to define ItemDict class and it's methods
"""

class ItemDict():
    def __init__(self, id = 1, num_of_items = 5):
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
        self._update_main_dict()
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
            item = I.Weapon(**d)
        elif d['item_type'] == 'Armor':
            item = I.Armor(**d)
        elif d['item_type'] == 'Consumable':
            item = I.Consumable(**d)
        return item

    def _update_main_dict(self):
        d = {}
        for i in range(self._id, self._num_of_items + 1):
            try:
                d[i] = self._build_item(i)
            except FileNotFoundError:
                print('File not found.  Please check to make sure it exists')

        self.all_items = d

    def _update_weapons(self):
        d = {}
        for i in self.all_items.values():
            if i.item_type == 'Weapon':
                d[i.id] = i
        self.weapons = d

    def _update_armor(self):
        d = {}
        for i in self.all_items.values():
            if i.item_type == 'Armor':
                d[i.id] = i
        self.armor = d

    def _update_consumables(self):
        d = {}
        for i in self.all_items.values():
            if i.item_type == 'Consumable':
                d[i.id] = i
        self.consumables = d
