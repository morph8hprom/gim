# #!/usr/bin/env python3
#
# import unittest
# import json
# from gim import item
#
# class ItemAttrbituesTestCase(unittest.TestCase):
# 
#     """
#     Contains tests for Item instance attributes
#     """
#     @classmethod
#     def setUpClass(cls):
#         """
#         Builds a dictionary of all items, a dictionary of only weapons,
#         a dictionary of only armor, and a dictionary of only consumables
#         """
#         # Create variables for starting id and number of items
#         start_id = 1
#         num_items = 5
#
#         # Create a variable to contain items of all type and
#         # use item_d() to create all item instances
#         cls.all_items = item_d(start_id, num_items)
#
#         # Create a variable to contain all items with item_type 'Weapon'
#         cls.weapon_dict = weapon_d(cls.all_items)
#
#         # Create a variable to contain all items with item_type 'Armor'
#         cls.armor_dict = armor_d(cls.all_items)
#
#         # Create a variable to contain all items with item_type 'Consumable'
#         cls.consumable_dict = consumable_d(cls.all_items)
#
#     def test_item_has_id(self):
#         """
#         Verifies that all item instances have the parameter 'id'
#         """
#
#         for i in self.all_items.values():
#             att = hasattr(i, 'id')
#             self.assertTrue(att)
#
#     def test_item_has_name(self):
#         """
#         Verifies that all item instances have the parameter 'name'
#         """
#
#         for i in self.all_items.values():
#             att = hasattr(i, 'name')
#             self.assertTrue(att)
#
#     def test_item_name_is_string(self):
#         """
#         Verifies that for all item instances, the parameter 'name' is a string
#         """
#
#         for i in self.all_items.values():
#             att = i.name
#             self.assertIsInstance(att, str)
#
#     def test_item_has_desc(self):
#         """
#         Verifies that all item instances have the parameter 'desc'
#         """
#
#         for i in self.all_items.values():
#             att = hasattr(i, 'desc')
#             self.assertTrue(att)
#
#     def test_item_desc_is_string(self):
#         """
#         Verifies that for all item instances, the paramter 'desc' is a string
#         """
#
#         for i in self.all_items.values():
#             att = i.name
#             self.assertIsInstance(att, str)
#
#
#     def test_item_has_item_type(self):
#         """
#         Verifies that all item instances have the parameter 'item_type'
#         """
#
#         for i in self.all_items.values():
#             att = hasattr(i, 'item_type')
#             self.assertTrue(att)
#
#     def test_item_type_is_string(self):
#         """
#         Verfies that for all item instances, the parameter 'item_type' is a string
#         """
#
#         for i in self.all_items.values():
#             att = i.name
#             self.assertIsInstance(att, str)
#
#     def test_weapon_has_damage(self):
#         """
#         Verifies that all weapon isntances have the parameter 'damage'
#         """
#
#         for i in self.weapon_dict.values():
#             att = hasattr(i, 'damage')
#             self.assertTrue(att)
#
#     def test_weapon_damage_is_int(self):
#         """
#         Verfies that for all weapon instances, the parameter 'damage' is an integer
#         """
#
#         for i in self.weapon_dict.values():
#             att = i.damage
#             self.assertIsInstance(att, int)
#
#     def test_weapon_has_weapon_type(self):
#         """
#         Verifies that all weapon instances have the parameter 'weapon_type'
#         """
#
#         for i in self.weapon_dict.values():
#             att = hasattr(i, 'weapon_type')
#             self.assertTrue(att)
#
#     def test_weapon_type_is_string(self):
#         """
#         Verifies that for all weapon instances, the parameter 'weapon_type' is a string
#         """
#
#         for i in self.weapon_dict.values():
#             att = i.weapon_type
#             self.assertIsInstance(att, str)
#
#     def test_armor_has_defense(self):
#         """
#         Verifies that all armor instances have the parameter 'defense'
#         """
#
#         for i in self.armor_dict.values():
#             att = hasattr(i, 'defense')
#             self.assertTrue(att)
#
#     def test_armor_defense_is_int(self):
#         """
#         Verifies that for all armor instances, the parameter defense is an integer
#         """
#
#         for i in self.armor_dict.values():
#             att = i.defense
#             self.assertIsInstance(att, int)
#
#     def test_armor_has_armor_slot(self):
#         """
#         Verifies that all armor instances have the parameter 'armor_slot'
#         """
#
#         for i in self.armor_dict.values():
#             att = hasattr(i, 'armor_slot')
#             self.assertTrue(att)
#
#     def test_armor_armor_slot_is_string(self):
#         """
#         Verifies that for all armor instances, the parameter 'armor_slot' is a string
#         """
#
#         for i in self.armor_dict.values():
#             att = i.armor_slot
#             self.assertIsInstance(att, str)
#
#     def test_consumable_has_first_effect(self):
#         """
#         Verifies that all consumable instances have the parameter 'effect'
#         """
#
#         for i in self.consumable_dict.values():
#             att = hasattr(i, 'first_effect')
#             self.assertTrue(att)
#
#     def test_consumable_effect_is_dict(self):
#         """
#         Verfies that for all consumable instances, the parameter 'effect' is a dictionary
#         """
#
#         for i in self.consumable_dict.values():
#             att = i.first_effect
#             self.assertIsInstance(att, dict)
#
#     def test_check_stat_method(self):
#         """
#         Checks that the _check_stat method is working properly
#         """
#
#         for i in self.consumable_dict.values():
#             # Assigns the value of the effect to the variable stat
#             stat = i._check_stat(i.first_effect)
#             if stat != None:
#                 ret = True
#             else:
#                 ret = False
#
#             self.assertTrue(ret)
