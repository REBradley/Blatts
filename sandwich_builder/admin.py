from django.contrib import admin

from.models import Condiment, Topping, Side, Sandwich, Cheese

# Register your models here.
admin.site.register(Sandwich)
admin.site.register(Condiment)
admin.site.register(Topping)
admin.site.register(Side)
admin.site.register(Cheese)