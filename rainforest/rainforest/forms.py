from django.forms import ModelForm
# from django.models import ModelForm
from rainforest.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price_in_cents']
