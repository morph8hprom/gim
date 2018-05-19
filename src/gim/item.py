#!/usr/bin/env python3
from pkg_resources import resource_string
import json
"""
File used to define item class, weapon class, armor class, and consumable class
"""

class Item:
    """
    Parameters and methods for the base Item class
    """

    def __init__(self, id = '1', name = 'test', desc = 'test desc', item_type = None):
        self.id = id
        self.name = name
        self.desc = desc
        self.item_type = item_type




class Weapon(Item):
    """
    Parameters and methods for the Weapon subclass
    """

    def __init__(self, id = 8, name = 'test weapon', desc = 'test desc', item_type = 'Weapon', damage = 0, weapon_type = None):
        super().__init__(id, name, desc, item_type)
        self.damage = damage
        self.weapon_type = weapon_type
        self.equipped = False



class Armor(Item):
    """
    Parameters and methods for the Armor subclass
    """

    def __init__(self, id = '10', name = 'test armor', desc = 'test desc', item_type = 'Armor', defense = 0, armor_slot = None):
        super().__init__(id, name, desc, item_type)
        self.item_type = 'Armor'
        self.defense = defense
        self.armor_slot = armor_slot
        self.equipped = False

class Consumable(Item):
    """
    Parameters and methods for the Consumable subclass
    """

    def __init__(self, id = '12', name = 'test consumable', desc = 'test desc', item_type = 'Consumable', first_effect = None, second_effect = None):
        super().__init__(id, name, desc, item_type)
        self.item_type = 'Consumable'
        self.first_effect = first_effect
        self.second_effect = second_effect

    def _check_stat(self, effect):
        """
        Checks which stat to modify
        """
        stat = effect.keys()
        return stat

    def _check_mod(self, effect):
        """
        Checks the value for the effect dict
        """
        mod_amount = effect.values()
        return mod_amount




def item_d(id, num_of_items):
    d = {}
    for i in range(id, num_of_items + 1):
        try:
            print('Gathering item data')
            d[i] = build_item(i)
            print('Successfully created item {} of {}'.format(i, num_of_items))
        except FileNotFoundError:
            print('File not found.  Please check to make sure it exists')

    return d


def weapon_d(item_dict):
    """
    Takes item dictionary as argument and filters out only weapons
    """
    d = {}
    for i in item_dict.values():
        if i.item_type == "Weapon":
            d[i.id] = i
    return d

def armor_d(item_dict):
    """
    Takes item dictionary as argument and filters out only armor
    """
    d = {}
    for i in item_dict.values():
        if i.item_type == "Armor":
            d[i.id] = i
    return d

def consumable_d(item_dict):
    """
    Takes item dictionary as argument and filters out only consumables
    """
    d = {}
    for i in item_dict.values():
        if i.item_type == "Consumable":
            d[i.id] = i
    return d

def build_item(id):
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
