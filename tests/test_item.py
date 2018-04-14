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
        # Create variables for starting id and number of items
        start_id = 1
        num_items = 5
        # Create a variable to contain items of all type and
        # use item_d() to create all item instances
        all_items = item_d(start_id, num_items)
        weapon_d = 
