#!/usr/bin/env python3

from item import *

"""
File used to define inventory class and and equipment subclass
"""

class Inventory():
    """
    Attributes and methods for the base Inventory class
    """

    def __init__(self):
        self.items = {}
        
