from django.forms import ModelForm
from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator

# from django.models import ModelForm
from rainforest.models import Product, Review

class ProductForm(ModelForm):
    min_validator = MinLengthValidator(10)
    max_validator = MaxLengthValidator(500, message='500! too long')

    name = forms.CharField()
    description = forms.CharField(validators=[min_validator, max_validator])
    price_in_cents = forms.IntegerField()

    class Meta:
        model = Product
        fields = ['name', 'description', 'price_in_cents']

class ReviewForm(ModelForm):
    name = forms.CharField(max_length = 255)
    comment = forms.CharField()

    class Meta:
        model = Review
        fields = ['name', 'comment']


    
        
