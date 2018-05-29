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
