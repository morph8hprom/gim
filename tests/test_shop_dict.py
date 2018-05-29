#!/usr/bin/env python3

import unittest
from gim import item as I
from gim import item_dict as Id
from gim import shop_dict as Sd

class ShopDictAttributesTestCase(unittest.TestCase):
    """
    Contains tests for ShopDict instance attributes
    """

    @classmethod
    def setUpClass(cls):
        """
        Builds test instance of ShopDict
        """
        cls.test_shop_dict = Sd.ShopDict()

    def test_shop_dict_has_items(self):
        att = hasattr(self.test_shop_dict, '_items')
        self.assertTrue(att)

    def test_shop_has_stock(self):
        att = hasattr(self.test_shop_dict, '_stock')
        self.assertTrue(att)

class ShopDictMethodsTestCase(unittest.TestCase):
    """
    Contains tests for ShopDict instance methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Builds a test instance of ShopDict
        """
        cls.test_shop_dict = Sd.ShopDict()
        # Test list for updating stock
        cls.test_list = [i for i in range(1,5)]


    def test_build_item(self):
        att = self.test_shop_dict._build_item(1)
        self.assertIsInstance(att, I.Item)

    def test_update_stock(self):
        self.test_shop_dict._items = self.test_list
        pre = len(self.test_shop_dict._stock)
        self.test_shop_dict._update_stock()
        post = len(self.test_shop_dict._stock)
        self.assertNotEqual(pre, post)
