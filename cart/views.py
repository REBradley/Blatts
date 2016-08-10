from django.shortcuts import render, get_object_or_404

from django.core.urlresolvers import reverse

from django.http import HttpResponse, HttpResponseRedirect

from sandwich_builder.models import Sandwich

from .cart import Cart


def show_cart(request):
    cart = Cart(request.session).items
    total = Cart(request.session).total
    
    context = {'cart':cart, 'total':total}
    
    return render(request, 'cart/show_cart.html', context)

def remove_from_cart(request, pk):
    cart = Cart(request.session)
    #product = Sandwich.objects.get(id=pk)
    cart.remove(pk)
    return HttpResponseRedirect(reverse('cart:show_cart'))