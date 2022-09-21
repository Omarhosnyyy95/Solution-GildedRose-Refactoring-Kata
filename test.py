# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from items import CreateItem

create_item = CreateItem()

class GildedRoseTest(unittest.TestCase):
    
    def test_conjured_quality(self):
        items = [ 
                create_item.create(name="Conjured Mana Cake", sell_in=3, quality=6),
                create_item.create(name="Conjured Mana Cake", sell_in=0, quality=6), 
                create_item.create(name="Conjured Mana Cake", sell_in=-1, quality=6),
                create_item.create(name="Conjured Mana Cake", sell_in=1, quality=60),
                create_item.create(name="Conjured Mana Cake", sell_in=1, quality=50),
                create_item.create(name="Conjured Mana Cake", sell_in=-1, quality=60),
                create_item.create(name="Conjured Mana Cake", sell_in=1, quality=1),
                create_item.create(name="Conjured Mana Cake", sell_in=1, quality=0),
                create_item.create(name="Conjured Mana Cake", sell_in=1, quality=-1)
            ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(4, items[0].quality)
        self.assertEqual(4, items[1].quality)
        self.assertEqual(2, items[2].quality)
        self.assertEqual(50, items[3].quality)
        self.assertEqual(50, items[4].quality)
        self.assertEqual(50, items[5].quality)
        self.assertEqual(0, items[6].quality)
        self.assertEqual(0, items[7].quality)
        self.assertEqual(0, items[8].quality)

if __name__ == '__main__':
    unittest.main()
