from django.shortcuts import render, get_object_or_404
from .models import Product
from cart.forms import CartAddProductForm

# Create your views here.
def index(request):
    products = Product.objects.all() # get all data
    context = {
        'products' : products,
    }
    return render(request, 'djangoecommerceapp/index.html', context)

def product_list(request):
    products = Product.objects.all()
    context = {
        'products' : products,
    }
    return render(request, 'djangoecommerceapp/products.html',context)

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id) # get single data
    cart_product_form = CartAddProductForm()
    context = {
        'product' : product,
        'cart_product_form' : cart_product_form
    }
    return render(request, 'djangoecommerceapp/single-product.html', context)