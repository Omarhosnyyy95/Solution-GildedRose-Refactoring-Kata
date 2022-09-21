# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from items import CreateItem

create_item = CreateItem()

class GildedRoseTest(unittest.TestCase):
    
    def test_normal_quality(self):
        items = [ 
                create_item.create(name="Elixir of the Mongoose", sell_in=3, quality=6),
                create_item.create(name="+5 Dexterity Vest", sell_in=0, quality=6), 
                create_item.create(name="Elixir of the Mongoose", sell_in=-1, quality=6),
                create_item.create(name="Elixir of the Mongoose", sell_in=1, quality=60),
                create_item.create(name="Elixir of the Mongoose", sell_in=-1, quality=60),
                create_item.create(name="Other Item", sell_in=2, quality=50),
                create_item.create(name="Other Item", sell_in=1, quality=1),
                create_item.create(name="Other Item", sell_in=1, quality=0),
                create_item.create(name="Other Item", sell_in=1, quality=-1)
            ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].quality)
        self.assertEqual(5, items[1].quality)
        self.assertEqual(4, items[2].quality)
        self.assertEqual(50, items[3].quality)
        self.assertEqual(50, items[4].quality)
        self.assertEqual(50, items[5].quality)
        self.assertEqual(0, items[6].quality)
        self.assertEqual(0, items[7].quality)
        self.assertEqual(0, items[8].quality)

    def test_conjured_quality(self):
        items = [ 
                create_item.create(name="Conjured Mana Cake", sell_in=3, quality=6),
                create_item.create(name="Conjured Mana Cake", sell_in=0, quality=6), 
                create_item.create(name="Conjured Mana Cake", sell_in=-1, quality=6),
                create_item.create(name="Conjured Mana Cake", sell_in=1, quality=60),
                create_item.create(name="Conjured Mana Cake", sell_in=-1, quality=60),
                create_item.create(name="Conjured Mana Cake", sell_in=2, quality=50),
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

    def test_aged_brie_quality(self):
        items = [ 
                create_item.create(name="Aged Brie", sell_in=3, quality=6),
                create_item.create(name="Aged Brie", sell_in=0, quality=6), 
                create_item.create(name="Aged Brie", sell_in=-1, quality=6),
                create_item.create(name="Aged Brie", sell_in=1, quality=60),
                create_item.create(name="Aged Brie", sell_in=1, quality=50),
                create_item.create(name="Aged Brie", sell_in=-1, quality=60),
                create_item.create(name="Aged Brie", sell_in=1, quality=-1)
            ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(7, items[0].quality)
        self.assertEqual(7, items[1].quality)
        self.assertEqual(7, items[2].quality)
        self.assertEqual(50, items[3].quality)
        self.assertEqual(50, items[4].quality)
        self.assertEqual(50, items[5].quality)
        self.assertEqual(0, items[6].quality)

    def test_sulfuras_quality(self):
        items = [ 
                create_item.create(name="Sulfuras, Hand of Ragnaros", sell_in=3, quality=80),
                create_item.create(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=70), 
                create_item.create(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=-10),
            ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(80, items[1].quality)
        self.assertEqual(80, items[2].quality)
    
    def test_backstage_quality(self):
        items = [ 
                create_item.create(name="Backstage passes to a TAFKAL80ETC concert", sell_in=8, quality=6), # 10 days or less
                create_item.create(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=6), # 10 days or less
                create_item.create(name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=6), # 5 days or less
                create_item.create(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=6), # 5 days or less
                create_item.create(name="Backstage passes to a TAFKAL80ETC concert", sell_in=1, quality=60), # item is never more than 50
                create_item.create(name="Backstage passes to a TAFKAL80ETC concert", sell_in=1, quality=50), # item is never more than 50
                create_item.create(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-1, quality=10), # quality drops to 0 after the concert
                create_item.create(name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=0), # Quality of an item is never negative
                create_item.create(name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=-1), # Quality of an item is never negative
                create_item.create(name="Backstage passes to a TAFKAL80ETC concert", sell_in=7, quality=48), # item is never more than 50
                create_item.create(name="Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=42), # days more than 10 and quality below 50
            ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)
        self.assertEqual(8, items[1].quality)
        self.assertEqual(9, items[2].quality)
        self.assertEqual(9, items[3].quality)
        self.assertEqual(50, items[4].quality)
        self.assertEqual(50, items[5].quality)
        self.assertEqual(0, items[6].quality)
        self.assertEqual(0, items[7].quality)
        self.assertEqual(0, items[8].quality)
        self.assertEqual(50, items[9].quality)
        self.assertEqual(42, items[10].quality)




if __name__ == '__main__':
    unittest.main()
