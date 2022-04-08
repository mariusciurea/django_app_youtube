from django import forms
from .models import Products

# class ProductsForm(forms.Form):
#     product = forms.CharField(label='Produs', max_length=100)
#     product1 = forms.CharField(label='Produs1', max_length=100)
#     product2 = forms.CharField(label='Produs2', max_length=100)
#     product3 = forms.CharField(label='Produs3', max_length=100)
#     cumparat = forms.BooleanField(required=False)

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product']