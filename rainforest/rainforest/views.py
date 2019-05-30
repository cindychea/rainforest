from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from datetime import date
from django.forms import ModelForm
from rainforest.models import *
from rainforest.forms import *

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

def new_product(request):
    product_form = ProductForm()
    context = {'product_form': product_form}
    response = render(request, 'new_product.html', context)
    return HttpResponse(response)

def create_product(request):
    new_product = ProductForm(request.POST)
    if(new_product.is_valid()):
        new_product.save()
        return HttpResponseRedirect('/')
    else:
        product_form = ProductForm()
        context = {'product_form': product_form, 'error_msg': 'You have invalid form, try again!'}
        response = render(request, 'new_product.html', context)
        return HttpResponse(response)


    # redirect()
    
    # request.POST


