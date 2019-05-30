from django.forms import ModelForm
from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator

# from django.models import ModelForm
from rainforest.models import Product

class ProductForm(ModelForm):
    min_validator = MinLengthValidator(10)
    max_validator = MaxLengthValidator(50,message='500! too long')
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price_in_cents']

    id = forms.HiddenInput()
    name = forms.CharField()
    description = forms.CharField(validators=[min_validator, max_validator])
    price_in_cents = forms.IntegerField()

