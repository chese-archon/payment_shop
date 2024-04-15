from django.shortcuts import render
from .forms import CustomerCreateForm
from cart.cart import Cart
from django.shortcuts import get_object_or_404, redirect
from .models import Customer, OrderItem

def add_customer(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CustomerCreateForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return render(request, 'orders/payment.html',
                          {'email':customer.email, 'id':customer.id})
    else:
        form = CustomerCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})

def save_item(request, id):
    cart = Cart(request)
    customer = get_object_or_404(Customer, pk=id)
    for item in cart:
        OrderItem.objects.create(customer=customer,
                                 product=item['product'],
                                 price=item['price'],
                                 quantity=item['quantity'])
    # clear the cart
    cart.clear()
    return redirect('djangoecommerceapp:product_list')
