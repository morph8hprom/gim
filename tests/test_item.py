#!/usr/bin/env python3

import unittest
import json
from src.item import *

class ItemAttrbituesTestCase(unittest.TestCase):

    """
    Contains tests for Item instance attributes
    """
    @classmethod
    def setUpClass(cls):
        """
        Builds a dictionary of all items, a dictionary of only weapons,
        a dictionary of only armor, and a dictionary of only consumables
        """
        # Create variables for starting id and number of items
        start_id = 1
        num_items = 5

        # Create a variable to contain items of all type and
        # use item_d() to create all item instances
        cls.all_items = item_d(start_id, num_items)

        # Create a variable to contain all items with item_type 'Weapon'
        cls.weapon_dict = weapon_d(cls.all_items)

        # Create a variable to contain all items with item_type 'Armor'
        cls.armor_dict = armor_d(cls.all_items)

        # Create a variable to contain all items with item_type 'Consumable'
        cls.consumable_dict = consumable_d(cls.all_items)

    def test_item_has_id(self):
        """
        Verifies that all item instances have the parameter 'id'
        """

        for i in self.all_items.values():
            att = hasattr(i, 'id')
            self.assertTrue(att)

    def test_item_has_name(self):
        """
        Verifies that all item instances have the parameter 'name'
        """

        for i in self.all_items.values():
            att = hasattr(i, 'name')
            self.assertTrue(att)

    def test_item_has_desc(self):
        """
        Verifies that all item instances have the parameter 'desc'
        """

        for i in self.all_items.values():
            att = hasattr(i, 'desc')
            self.assertTrue(att)

    def test_item_has_item_type(self):
        """
        Verifies that all item instances have the parameter 'item_type'
        """

        for i in self.all_items.values():
            att = hasattr(i, 'item_type')
            self.assertTrue(att)

    def test_weapon_has_damage(self):
        """
        Verifies that all weapon isntances have the parameter 'damage'
        """

        for i in self.weapon_dict.values():
            att = hasattr(i, 'damage')
            self.assertTrue(att)

    def test_weapon_has_weapon_type(self):
        """
        Verifies that all weapon instances have the parameter 'weapon_type'
        """

        for i in self.weapon_dict.values():
            att = hasattr(i, 'weapon_type')
            self.assertTrue(att)

    def test_armor_has_defense(self):
        """
        Verifies that all armor instances have the parameter 'defense'
        """

        for i in self.armor_dict.values():
            att = hasattr(i, 'defense')
            self.assertTrue(att)

    def test_armor_has_armor_slot(self):
        """
        Verifies that all armor instances have the parameter 'armor_slot'
        """

        for i in self.armor_dict.values():
            att = hasattr(i, 'armor_slot')
            self.assertTrue(att)
            
    def test_consumable_has_effect(self):
        """
        Verifies that all consumable instances have the parameter 'effect'
        """

        for i in self.consumable_dict.values():
            att = hasattr(i, 'effect')
            self.assertTrue(att)
