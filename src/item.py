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
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc




class Weapon(Item):
    """
    Parameters and methods for the Weapon subclass
    """
    def __init__(self, name, desc, damage, weapon_type):
        super().__init__(name, desc)
        self.damage = damage
        self.weapon_type = weapon_type


class Armor(Item):
    """
    Parameters and methods for the Armor subclass
    """
    def __init__(self, name, desc, defense, armor_slot):
        super().__init__(name, desc)
        self.defense = defense
        self.armor_slot = armor_slot

class Consumable(Item):
    """
    Parameters and methods for the Consumable subclass
    """
    def __init__(self, name, desc, effect):
        super().__init__(name, desc)
        self.effect = effect

def item_d(id, num_of_items):
    d = {}
    for i in range(id, num_of_items):
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
        if i[item_type] == 'Weapon':
            d[i[id]] = i
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
