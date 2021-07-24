from django import forms
from django.forms import widgets
from .models import *

class CatForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
        }
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields ='__all__'

        widgets = {
            'titel' : forms.TextInput(attrs={'class':'form-control'}),
            'company' : forms.TextInput(attrs={'class':'form-control'}),
            'photo_product' : forms.FileInput(attrs={'class':'form-control'}),
            'photo_company' : forms.FileInput(attrs={'class':'form-control'}),
            'quantity' : forms.NumberInput(attrs={'class':'form-control'}),
            'price' : forms.NumberInput(attrs={'class':'form-control'}),
            'discount' : forms.NumberInput(attrs={'class':'form-control','id':'dis'}),
            'discount_for' : forms.NumberInput(attrs={'class':'form-control','id':'disfor'}),
            'total' : forms.NumberInput(attrs={'class':'form-control','id':'total'}),
            'active' : forms.CheckboxInput(attrs={'class':'form-control'}),
            'status' : forms.Select(attrs={'class':'form-control'}),
            'category' : forms.Select(attrs={'class':'form-control'}),
           
        }