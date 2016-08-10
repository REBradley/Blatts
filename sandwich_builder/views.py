from django.shortcuts import render, get_object_or_404

from django.db.models import F

from django.core.urlresolvers import reverse

from django.http import HttpResponse, HttpResponseRedirect

from .models import Sandwich, Cheese, Condiment, Side, Topping, Base, Bread

from .forms import SandwichForm, QuantityForm

from cart.cart import Cart


def sandwich_index(request):
    request.session.set_expiry(0)
    
    base_selections = Base.objects.all()
    context = {'base_selections':base_selections}
    return render(request, 'sandwich_builder/sandwich_index.html', context)

def burger_constructor(request, base):
    form = SandwichForm(initial={'base': base})
    form2 = QuantityForm()
    
    sand_base = get_object_or_404(Base, pk=base)
    return render(request, 'sandwich_builder/sandwich_constructor.html',
                  {'form':form, 'form2':form2, 'base':sand_base})

def add_sandwich(request, base):
    cart = Cart(request.session)
    
    sand_base = get_object_or_404(Base, pk=base)
    form = SandwichForm(request.POST, initial={'base': base})
    form2 = QuantityForm(request.POST)
    
    if form.is_valid() and form2.is_valid():
        bread = form.cleaned_data['bread']
        toppings = form.cleaned_data['toppings']
        condiments = form.cleaned_data['condiments']
        cheeses = form.cleaned_data['cheeses']
        side= form.cleaned_data['side']
        
        quantity = form2.cleaned_data['quantity']
        
        sandwich = Sandwich()
        sandwich.base= sand_base
        sandwich.bread= bread
        sandwich.save()
        
        sandwich.side= side
        sandwich.toppings= toppings
        sandwich.condiments= condiments
        sandwich.cheeses= cheeses
        sandwich.save()
        
        product = sandwich 
        cart.add(product, price=sandwich.price, quantity=quantity)
        return HttpResponseRedirect(reverse('cart:show_cart'))
    
    return render(request, 'sandwich_builder/sandwich_constructor.html',
                  {'base': sand_base, 'form':form})