from django.core.management.base import BaseCommand
from sandwich_builder.models import Condiment, Cheese, Sandwich, Side, Topping
from sandwich_builder.models import Base, Bread

class Command(BaseCommand):
    
    help = 'Populates necessary data'
    
    def create_condiments(self):
        no_condiments = Condiment(condiments='No Condiments')
        no_condiments.save()
        
        y_must = Condiment(condiments='Yellow Mustard')
        y_must.save()
        
        d_must = Condiment(condiments='Dijon Mustard')
        d_must.save()
        
        s_must = Condiment(condiments='Spicy Deli Mustard')
        s_must.save()
        
        mayo = Condiment(condiments='Mayo')
        mayo.save()
        
        russian = Condiment(condiments='1000 Island')
        russian.save()
    
    
    
    def create_toppings(self):
        no_toppings = Topping(toppings='No Toppings', price = 0.50)
        no_toppings.save()
        
        tomato = Topping(toppings='Tomato', price = 0.50)
        tomato.save()
        
        avocado = Topping(toppings='Avocado', price = 1.25)
        avocado.save()
        
        extra_meat = Topping(toppings='Extra Meat', price = 2.00)
        extra_meat.save()
        
        cole_slaw = Topping(toppings='Cole Slaw', price = 1.50)
        cole_slaw.save()
        
        onion = Topping(toppings='Onion', price = 0.00)
        onion.save()
        
        lett = Topping(toppings='Lettuce', price = 0.00)
        lett.save()
    
    
    
    def create_cheeses(self):
        no_cheese = Cheese(cheeses='No Cheese', price = 0.90)
        no_cheese.save()
        
        ched = Cheese(cheeses='Cheddar', price = 0.90)
        ched.save()
        
        swiss = Cheese(cheeses='Swiss', price = 0.90)
        swiss.save()
        
        prov = Cheese(cheeses='Provolone', price = 0.90)
        prov.save()
        
        muens = Cheese(cheeses='Muenster', price = 0.90)
        muens.save()
        
    
    
    def create_sides(self):
        no_side = Side(sides='No Side')
        no_side.save()
        
        slaw = Side(sides='Cole Slaw')
        slaw.save()
        
        fruit = Side(sides='Fruit Salad')
        fruit.save()
        
        potato = Side(sides='Potato Salad')
        potato.save()
        
        chips = Side(sides='Kettle Chips')
        chips.save()
        
        macaroni = Side(sides='Macaroni Salad')
        macaroni.save()
        
    
    def create_bases(self):
        pastrami = Base(bases='Pastrami', price=13.95)
        pastrami.save()
        
        turkey = Base(bases='Turkey', price=12.95)
        turkey.save()
        
        corned_beef = Base(bases='Corned_Beef', price=13.95)
        corned_beef.save()
    
    def create_breads(self):
        rye = Bread(breads='Rye', price=0.00)
        rye.save()
        
        sourdough = Bread(breads='Sourdough', price=0.00)
        sourdough.save()
        
        wheat = Bread(breads='Wheat', price=0.00)
        wheat.save()
        
        white = Bread(breads='White', price=0.00)
        white.save()
        
        egg = Bread(breads='Egg', price=0.00)
        egg.save()
        
        pump = Bread(breads='Pumpernickel', price=0.00)
        pump.save()
        
        french = Bread(breads='French Roll', price=0.90)
        french.save()
        
        kaiser = Bread(breads='Kaiser Roll', price=0.90)
        kaiser.save()
        
        rosemary = Bread(breads='Rosemary', price=0.90)
        rosemary.save()
        
        no_bread = Bread(breads='No Bread', price=0.00)
        no_bread.save()
    
    def handle(self, *args, **options):
        self.create_sides()
        self.create_condiments()
        self.create_toppings()
        self.create_cheeses()
        self.create_bases()
        self.create_breads()
