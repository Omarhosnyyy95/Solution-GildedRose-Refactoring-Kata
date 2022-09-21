class CreateItem(object):
    def create(self, name, sell_in, quality):
        
        # special cases
        if name == "Aged Brie": 
            return AgedBrie(name, sell_in, quality)
        if name == "Conjured Mana Cake": 
            return Conjured(name, sell_in, quality)
        if name == "Sulfuras, Hand of Ragnaros": 
            return Sulfuras(name, sell_in, quality)
        if name == "Backstage passes to a TAFKAL80ETC concert": 
            return Backstage(name, sell_in, quality)
        
        # if not a special case
        return BaseItem(name, sell_in, quality)

class BaseItem(object):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self.MAX_QUALITY = 50
        self.MIN_QUALITY = 0

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


    def update_quality(self):
        if  50 > self.quality > 0:
            if self.sell_in < 0:
                if self.quality < 2:
                    self.quality = 0
                else:
                    self.quality = self.quality - 2
            else:
                self.quality = self.quality - 1
        elif self.quality >= 50:
            self.quality = 50
        else:
            self.quality = 0
               
        self.sell_in = self.sell_in - 1

class AgedBrie(BaseItem):
    def update_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1
        elif self.quality >= 50:
            self.quality = 50
        else:
            self.quality = 0


        self.sell_in = self.sell_in - 1

class Sulfuras(BaseItem):
    def update_quality(self):
        self.quality = 80
        self.sell_in = self.sell_in - 1

class Backstage(BaseItem):
    def update_quality(self):
        
        if self.sell_in < 0:
            self.quality = 0

        elif self.quality <= 0:
            self.quality = 0   

        elif self.sell_in <= 10:
            if self.sell_in <= 5 and (self.quality + 3) <= 50:
                self.quality += 3

            elif (self.quality + 2) <= 50:
                self.quality += 2

            else:
                self.quality = 50


        self.sell_in = self.sell_in - 1

class Conjured(BaseItem):
    def update_quality(self):
        if 50 > self.quality > 0:
            
            # "Conjured" items degrade in Quality twice as fast as normal items
            if self.sell_in < 0:
                self.quality = self.quality - 4 if self.quality > 3 else 0
            else:
                self.quality = self.quality - 2 if self.quality > 1 else 0
            if self.quality < 0:
                self.quality = 0

        elif self.quality >= 50:
            self.quality = 50
        else:
            self.quality = 0

        self.sell_in = self.sell_in - 1