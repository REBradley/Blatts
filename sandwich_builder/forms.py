from django import forms


from sandwich_builder.models import Sandwich, Base

class SandwichForm(forms.ModelForm):
    class Meta:
        model = Sandwich
        fields = ['bread', 'cheeses', 'condiments', 'toppings', 'side']

class QuantityForm(forms.Form):
    quantity = forms.IntegerField(label='Quantity',
                                  initial=1, min_value = 1, max_value = 5)
