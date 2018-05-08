#!/usr/bin/env python3

from item import *

"""
File used to define inventory class and related methods
"""

class Inventory():
    """
    Attributes and methods for the base Inventory class
    """

    def __init__(self):
        self.items = {}

    def __iter__(self):
        # Defines item as an iterable
        return iter(self.items.items())

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        # Overwrites __contains__ method for easy use of 'if x in items'
        return item.id in self.items

    def __getitem__(self, item):
        # Overwrites __getitem__ method for easy access to individual items
        return self.items[item.id]

    # def _get_quant(self, item_id):
    #     # Returns the quantity of item
    #     quant  = self.items[item_id][quant]
    #     return quant

    def _add_item(self, item):
        # Adds item to inventory
        self.items[item.id] = item
