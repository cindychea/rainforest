from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
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
    review_form = ReviewForm(use_required_attribute=False)
    context = {'product': product, 'review_form': review_form}
    return render(request, 'product.html', context)

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

    return render(request, 'edit_product.html', {
        'product_form': product_form,
        'product_id': id
    })

def update_product(request, id):
    product = Product.objects.get(id=id)
    product_form = ProductForm(request.POST, instance=product)

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

def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    # context = {'delete_msg': f'You have deleted {product.name}'}
    # response = render(request, 'index.html', context)
    return HttpResponseRedirect('/')

# def review_form(request,id):
#     review_form = ReviewForm()
#     context = {'review_form': review_form}
#     response = render(request, 'new_review.html', context)
#     return HttpResponse(response)

def new_review(request, id):
    product = Product.objects.get(id=id)
    form = ReviewForm(request.POST, use_required_attribute=False)
    print(request.POST)
    if form.is_valid():
        review = form.instance
        review.product = Product.objects.get(id=id)
        review.save()
        return redirect('view_product', id=id)
    else:
        context = {'error_msg': 'You have invalid form, try again!', 'product': product, 'review_form': form}
        response = render(request, 'product.html', context)
        return HttpResponse(response)

def edit_review(request, id, review_id):
    product = Product.objects.get(id=id)
    review = Review.objects.get(id=review_id)

    form = ReviewForm(request.POST, instance=review)
    print('review::', review, '\n form::', form)

    if form.is_valid():
        form.save()
        return redirect('view_product', id=id)
    else:
        return render(request, 'edit_review.html', {
            'review_form': form,
            'product_id': id, 
            'review_id': review_id,
            'product': product,
            'review': review,
            'error_msg': 'You have invalid form, try again!'
        })


def delete_review(request, review_id):
    review = Review.objects.get(id=review_id)
    review.delete()
    # context = {'delete_msg': f'You have deleted {product.name}'}
    # response = render(request, 'index.html', context)
    return HttpResponseRedirect('/')

