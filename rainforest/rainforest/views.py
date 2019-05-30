from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from datetime import date
from django.forms import ModelForm
from rainforest.models import *

def root(request):
    products =  Product.objects.all()
    context = {'products': products}
    response = render(request, 'index.html', context)
    return HttpResponse(response) 

def view_product(request, id1):
    
    product = Product.objects.get(id=id1)
    context = {'product': product}
    response = render(request, 'product.html', context)
    return HttpResponse(response)


