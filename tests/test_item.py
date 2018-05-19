#!/usr/bin/env python3

import unittest
from gim import item as I

class ItemAttrbituesTestCase(unittest.TestCase):
    """
    Contains tests for Item instance attributes
    """

    @classmethod
    def setUpClass(cls):
        """
        Builds test instance of Item using default parameters
        """
        cls.test_item = I.Item()

    def test_item_has_id(self):
        att = hasattr(self.test_item, 'id')
        self.assertTrue(att)

    def test_item_has_name(self):
        att = hasattr(self.test_item, 'name')
        self.assertTrue(att)

    def test_item_has_desc(self):
        att = hasattr(self.test_item, 'desc')
        self.assertTrue(att)

    def test_item_has_item_type(self):
        att = hasattr(self.test_item, 'item_type')
        self.assertTrue(att)

class WeaponAttributesTestCase(unittest.TestCase):
    """
    Contains tests for Weapon instance attributes
    """

    @classmethod
    def setUpClass(cls):
        """
        Builds test instance of Weapon using default parameters
        """
        cls.test_weapon = I.Weapon()

    def test_weapon_has_id(self):
        att = hasattr(self.test_weapon, 'id')
        self.assertTrue(att)

    def test_weapon_has_name(self):
        att = hasattr(self.test_weapon, 'name')
        self.assertTrue(att)

    def test_weapon_has_desc(self):
        att = hasattr(self.test_weapon, 'desc')
        self.assertTrue(att)

    def test_weapon_has_item_type(self):
        att = hasattr(self.test_weapon, 'item_type')
        self.assertTrue(att)

    def test_weapon_has_damage(self):
        att = hasattr(self.test_weapon, 'damage')
        self.assertTrue(att)

    def test_weapon_has_weapon_type(self):
        att = hasattr(self.test_weapon, 'weapon_type')
        self.assertTrue(att)

    def test_weapon_has_equipped(self):
        att = hasattr(self.test_weapon, 'equipped')
        self.assertTrue(att)

class ArmorAttributesTestCase(unittest.TestCase):
    """
    Contains tests for Armor instance attributes
    """

    @classmethod
    def setUpClass(cls):
        """
        Builds a test instance of Armor using default parameters
        """
        cls.test_armor = I.Armor()

    def test_armor_has_id(self):
        att = hasattr(self.test_armor, 'id')
        self.assertTrue(att)

    def test_armor_has_name(self):
        att = hasattr(self.test_armor, 'name')
        self.assertTrue(att)

    def test_armor_has_desc(self):
        att = hasattr(self.test_armor, 'desc')
        self.assertTrue(att)

    def test_armor_has_item_type(self):
        att = hasattr(self.test_armor, 'item_type')
        self.assertTrue(att)

    def test_armor_has_defense(self):
        att = hasattr(self.test_armor, 'defense')
        self.assertTrue(att)

    def test_armor_has_armor_slot(self):
        att = hasattr(self.test_armor, 'armor_slot')
        self.assertTrue(att)

    def test_armor_has_equipped(self):
        att = hasattr(self.test_armor, 'equipped')
        self.assertTrue(att)

class ConsumableAttributesTestCase(unittest.TestCase):
    """
    Contains tests for Consumable instance attributes
    """

    @classmethod
    def setUpClass(cls):
        """
        Builds test instance of Consumable using default parameters
        """
        cls.test_consumable = I.Consumable()

    def test_consumable_has_id(self):
        att = hasattr(self.test_consumable, 'id')
        self.assertTrue(att)

    def test_consumable_has_name(self):
        att = hasattr(self.test_consumable, 'name')
        self.assertTrue(att)

    def test_consumable_has_desc(self):
        att = hasattr(self.test_consumable, 'desc')
        self.assertTrue(att)

    def test_consumable_has_item_type(self):
        att = hasattr(self.test_consumable, 'item_type')
        self.assertTrue(att)

    def test_consumable_has_first_effect(self):
        att = hasattr(self.test_consumable, 'first_effect')
        self.assertTrue(att)

    def test_consumable_has_second_effect(self):
        att = hasattr(self.test_consumable, 'second_effect')
        self.assertTrue(att)

# class ConsumableMethodsTestCase(unittest.TestCase):
#     """
#     Contains tests for Consumable instance methods
#     """
#
#     @classmethod
#     def setUpClass(cls):
#         """
#         Builds a test instance of Consumable using default parameters
#         """
#         cls.test_consumable = I.Consumable()
#
#     def test_check_stat(self):
# 
