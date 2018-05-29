#!/usr/bin/env python3

import json
from gim import item as I
from gim import item_dict as Id

class ShopDict():
    def __init__(self, items = [], stock = {}):
        self._items = items
        self._stock = stock
        self._update_stock()

    def __iter__(self):
        return iter(self._items.items())

    def __len__(self):
        return len(self._stock)

    def __contains__(self, item):
        return item in self._items

    def __getitem__(self, item):
        return self._items[item.id]

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

    def _update_stock(self):
        d = {}
        for i in self._items:
            try:
                d[i] = self._build_item(i)
            except FileNotFoundError:
                print('File not found.  Please check to make sure it exists')
