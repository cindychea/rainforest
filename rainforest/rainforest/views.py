from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from datetime import date
from django.forms import ModelForm
from rainforest.models import *
from rainforest.forms import *

def root(request):
    products = Product.objects.all()
    context = {'products': products}
    response = render(request, 'index.html', context)
    return HttpResponse(response) 

def view_product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product.html', {'product': product})

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

def edit_product(request, id):
    product = Product.objects.get(id=id)
    product_form = ProductForm(instance=product)

<<<<<<< HEAD
    return render(request, 'edit_product.html', {
        'product_form': product_form,
        'product_id': id
    })

def update_product(request, id):
    product = Product.objects.get(id=id)
    product_form = ProductForm(request.POST, instance=product)
=======
def update_product(request):
    updated_product = ProductForm(instance=None)
    # updated_product = ProductForm(request.POST)
    if(updated_product.is_valid()):
        updated_product.save()
        return redirect('view_product', id=request.POST['id'])
        # return HttpResponseRedirect('/')
    else:
        product_to_edit = Product.objects.get(id=request.POST['id'])
        product_form = ProductForm(instance=product_to_edit)
        context = {'product_form': product_form, 'error_msg': 'You have invalid form, try again!'}
        response = render(request, 'edit_product.html', context)
        return HttpResponse(response)
>>>>>>> 3dc0c8e9981b36a551c2e92d1ac162c43dc20df3

    # Get the product by id (from parameter in url)
    # Find the instance
    # If instance changes are valid
    #   save and redirect
    # else
    #   re-render the form with the values and the error message

    if product_form.is_valid():
        product_form.save()
        return redirect('view_product', id=id) # Instance or not?
    else:
        return render(request, 'edit_product.html', {
            'product_form': product_form,
            'product_id': id,
            'error_msg': 'You have invalid form, try again!'
        })


