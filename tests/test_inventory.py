#!/usr/bin/env python3

import unittest
import json
from src.item import *
from src.inventory import *


class InventoryAttributesTestCase(unittest.TestCase):
    """
    Contains test for Inventory instance attributes
    """

    @classmethod
    def setUpClass(cls):
        """
        Builds a dictionary of all items, a dictionary of only weapons,
        a dictionary of only armor, and a dictionary of only consumables
        Then creates an inventory instance to store item instances
        """

        start_id = 1
        num_of_items = 5

        cls.all_items = item_d(start_id, num_of_items)

        cls.weapon_dict = weapon_d(cls.all_items)

        cls.armor_dict = armor_d(cls.all_items)

        cls.consumable_dict = consumable_d(cls.all_items)

        cls.inventory = Inventory()


    def test_inventory_has_items(self):
        att = hasattr(self.inventory, 'items')
        self.assertTrue(att)

class InventoryMethodsTestCase(unittest.TestCase):

    """
    Contains test for inventory methods
    """

    @classmethod
    def setUpClass(cls):


        """
        Builds a dictionary of all items, a dictionary of only weapons,
        a dictionary of only armor, and a dictionary of only consumables
        Then creates an inventory instance to store item instances
        """

        start_id = 1
        num_of_items = 5

        cls.all_items = item_d(start_id, num_of_items)

        cls.weapon_dict = weapon_d(cls.all_items)

        cls.armor_dict = armor_d(cls.all_items)

        cls.consumable_dict = consumable_d(cls.all_items)

        cls.inventory = Inventory()

    def test_inventory_len_returns_correct_number(self):
        a = self.inventory.__len__()
        b = len(self.inventory.items.items())
        self.assertEqual(a, b)

    def test_inventory_is_iterable(self):
        try:
            iter(self.inventory)
            att = True
        except TypeError:
            att = False
        self.assertTrue(att)

    def test_inventory_add_item_adds_item(self):
        for i in self.all_items.values():
            # Adds item from values list to inventory
            self.inventory._add_item(i)
            item = self.inventory[i]

            # Verifies that items are identical
            self.assertEqual(i, item)


    def test_contains_method(self):
        for i in self.all_items.values():
            self.inventory._add_item(i)
            att = i in self.inventory
            self.assertTrue(att)
