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
        self._id = id
        self._name = name
        self._desc = desc
        self._item_type = item_type

    def __repr__(self):
        return 'Id:{}\n Name:{}\n Desc:{}\n Item Type:{}'.format(self.id, self.name, self.desc, self.item_type)





class Weapon(Item):
    """
    Parameters and methods for the Weapon subclass
    """

    def __init__(self, id = 8, name = 'test weapon', desc = 'test desc', item_type = 'Weapon', damage = 0, weapon_type = None, two_handed = False):
        super().__init__(id, name, desc, item_type)
        self.damage = damage
        self.weapon_type = weapon_type
        self.two_handed = two_handed
        self.equipped = False






class Armor(Item):
    """
    Parameters and methods for the Armor subclass
    """

    def __init__(self, id = '10', name = 'test armor', desc = 'test desc', item_type = 'Armor', defense = 0, slot = None):
        super().__init__(id, name, desc, item_type)
        self.defense = defense
        self._slot = slot
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
