from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from mainapp.models import Product
from django.contrib.auth.decorators import login_required

from .models import CartItem

# implementing AJAX to update cart item quantity without refresh
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

# Create your views here.


def viewCart(request):
    template= 'my_cart.html'
    cart_items = CartItem.objects.filter(user = request.user)
    total_price = sum(item.sub_total for item in cart_items)
    context = {
        'items' : cart_items,
        'total_price' : total_price
    }
    return render(request, template, context)

@login_required
def addToCart(request, product_id):
    this_product = Product.objects.get(id = product_id)
    this_user = request.user 
    cart_item, created_at = CartItem.objects.get_or_create(product = this_product, user = this_user)
    cart_item.quantity += 1
    cart_item.save()
    
    return redirect(reverse_lazy('my_cart'))

def remFromCart(request, cart_item_id):
    this_cart_item = CartItem.objects.get(id = cart_item_id)
    this_cart_item.delete()
    return redirect(reverse_lazy('my_cart'))



# function based views for implementing the API endpoints for cart quantity updations
@login_required
def addQuantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    overall_total = sum(item.get_total() for item in CartItem.objects.filter(user=request.user))
    context = {
        'quantity': cart_item.quantity, 
        'total_price': cart_item.get_total(), 
        'overall_total': overall_total
        }
    return JsonResponse(context)

@login_required
def remQuantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        overall_total = sum(item.get_total() for item in CartItem.objects.filter(user=request.user))
        context = {
            'quantity': cart_item.quantity, 
            'total_price': cart_item.get_total(), 
            'overall_total': overall_total}
        return JsonResponse(context)
    else:
        cart_item.delete()
        overall_total = sum(item.get_total() for item in CartItem.objects.filter(user=request.user))
        context = {
            'quantity': 0, 
            'total_price': 0, 
            'overall_total': overall_total
            }
        return JsonResponse(context)