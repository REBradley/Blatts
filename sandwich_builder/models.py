from __future__ import unicode_literals
from django.db import models

from decimal import Decimal

class PricedItem(models.Model):
    """
    An abstract base class model that provides price fields
    for every item sold.
    """
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    
    class Meta:
        abstract = True

class Condiment(PricedItem):
    """
    Class providing the different types of spreadable sandwich additions.
    """
    condiments = models.CharField(max_length = 30, blank=True)
    def __unicode__(self):
        return self.condiments

class Topping(PricedItem):
    """
    Class providing the different types of non-spreadable sandwich additions.
    """
    toppings = models.CharField(max_length= 30, blank=True)
    def __unicode__(self):
        return self.toppings

class Cheese(PricedItem):
    """
    Class providing the different cheese additions.
    """
    cheeses = models.CharField(max_length= 30, blank=True)
    def __unicode__(self):
        return self.cheeses

class Side(PricedItem):
    """
    Class providing the different available sides on offer.
    """
    sides = models.CharField(max_length= 30)
    def __unicode__(self):
        return self.sides
     
class Base(PricedItem):
    """
    Class that defines the type of 'filling' for a sandwich.
    A main sandwich type identifier, along with Bread.
    """
    bases = models.CharField(max_length = 10, primary_key=True)
    
    def human_readable(self):
        return self.bases.replace('_', ' ')
    
    def __unicode__(self):
        return self.bases

class Bread(PricedItem):
    """
    Class that defines the type of bread for a sandwich.
    A main sandwich type identifier, along with Base.
    """
    breads = models.CharField(max_length = 10)
    toasted = models.NullBooleanField()
    def __unicode__(self):
        return self.breads

class Sandwich(models.Model):
    """
    The raison d'etre of this module. Defines sandwiches in terms
    of constituent classes, which can be mixed and matched in any quantity.
    """
    bread = models.ForeignKey(Bread, on_delete=models.CASCADE)
    base = models.ForeignKey(Base, on_delete=models.CASCADE)
    
    condiments = models.ManyToManyField(Condiment, default='No Condiments', blank=True)
    toppings = models.ManyToManyField(Topping, default='No Toppings', blank=True)
    cheeses = models.ManyToManyField(Cheese, default='No Cheese', blank=True)
    side = models.ForeignKey(Side, default=0, blank=True)
    
    
    
    @property
    def get_extras_price(self):
        add_ons = []
        total = Decimal(0.00)
        
        for item in self.toppings.all():
            add_ons.append(item.price)
            
        for item in self.cheeses.all():
            add_ons.append(item.price)
            
        for price in add_ons:
            total += price
            
        return total
    
    @property
    def price(self):
        return self.base.price + self.bread.price + self.get_extras_price
    
    class Meta:
        verbose_name_plural='sandwiches'
    
    def __unicode__(self):
        return "%s on %s (%s)" % (self.base.human_readable(), self.bread, self.side)