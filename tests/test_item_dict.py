#!/usr/bin/env python3

import unittest
import json
from gim import item_dict as i_d

class ItemDictAttributeTestCase(unittest.TestCase):
    """
    Contains tests for ItemDict instance attributes
    """

    @classmethod
    def setUpClass(cls):
        """
        Builds a test instance of ItemDict
        """
        cls.test_item_d = i_d.ItemDict()

    def test_item_d_has_all_items(self):
        att = hasattr(self.test_item_d, 'all_items')
        self.assertTrue(att)

    def test_item_d_has_weapons(self):
        att = hasattr(self.test_item_d, 'weapons')
        self.assertTrue(att)

    def test_item_d_has_armor(self):
        att = hasattr(self.test_item_d, 'armor')
        self.assertTrue(att)

    def test_item_d_has_consumables(self):
        att = hasattr(self.test_item_d, 'consumables')
        self.assertTrue(att)

class ItemDictMethodsTestCase(unittest.TestCase):

    """
    Contains tests for ItemDict methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Builds a test instance of ItemDict
        """
        cls.test_item_d = i_d.ItemDict()

    def test_item_d_method_for_weapons(self):
        # Assumes that character data file with item_id has the attribute item_type = Weapon
        # if it does not, change item_id to a file which does

        item_id = 1
        test_item = self.test_item_d._build_item(item_id)
        att = isinstance(test_item, i_d.I.Weapon)
        self.assertTrue(att)

    def test_item_d_method_for_armor(self):
        # Assumes that character data file with item_id has the attribute item_type = Armor
        # if it does not, change item_id to a file which does

        item_id = 3
        test_item = self.test_item_d._build_item(item_id)
        att = isinstance(test_item, i_d.I.Armor)
        self.assertTrue(att)

    def test_item_d_method_for_consumable(self):
        # Assumes that character data file with item_id has the attribute item_type = Consumable
        # if it does not, change item_id to a file which does

        item_id = 5
        test_item = self.test_item_d._build_item(item_id)
        att = isinstance(test_item, i_d.I.Consumable)
        self.assertTrue(att)

    def test_update_main_dict(self):
        self.test_item_d._num_of_items = 6
        pre_update = len(self.test_item_d.all_items)
        self.test_item_d._update_main_dict()
        post_update = len(self.test_item_d.all_items)
        self.assertNotEqual(pre_update, post_update)

    def test_update_weapons(self):
        test_item = i_d.I.Weapon()
        self.test_item_d.all_items[test_item._id] = test_item
        pre_update = len(self.test_item_d.weapons)
        self.test_item_d._update_weapons()
        post_update = len(self.test_item_d.weapons)
        self.assertNotEqual(pre_update, post_update)

    def test_update_armor(self):
        test_item = i_d.I.Armor()
        self.test_item_d.all_items[test_item._id] = test_item
        pre_update = len(self.test_item_d.armor)
        self.test_item_d._update_armor()
        post_update = len(self.test_item_d.armor)
        self.assertNotEqual(pre_update, post_update)

    def test_update_consumables(self):
        test_item = i_d.I.Consumable()
        self.test_item_d.all_items[test_item._id] = test_item
        pre_update = len(self.test_item_d.consumables)
        self.test_item_d._update_consumables()
        post_update = len(self.test_item_d.consumables)
        self.assertNotEqual(pre_update, post_update)
