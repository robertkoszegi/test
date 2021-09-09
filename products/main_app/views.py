from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Product 
from .forms import ProductForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def products_index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})

def products_detail(request, product_id):
  product = Product.objects.get(id=product_id)
  return render(request, 'products/detail.html', { 'product': product })

def product_create(request):
    context = {}
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/products/")

    context['form'] = form
    return render(request, "create_product.html", context)

def product_delete(request, product_id=None):
    product=get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return HttpResponseRedirect('/products/')