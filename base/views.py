from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login

from .models import Product, CartItem


def home(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        quantity = 0
        for cart_item in cart_items:
            quantity += cart_item.quantity
        context = {
            "products": products,
            "cart_quantity": quantity,
        }
    return render(request, 'base/home.html', context)


def login(request):
    # check type of request
    if request.method == 'POST':
        # login flow
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(dir(user))
            auth_login(request, user)
            return redirect('base-home')

    # if not from form, render form
    return render(request, 'base/login.html')


def logout(request):
    auth_logout(request)
    return redirect('base-home')


def register(request):
    return HttpResponse("Hello, world. You're at the base register.")


def product(request, id):
    product = Product.objects.get(id=id)

    discount = 0.15
    final_price = int(product.price) - discount * int(product.price)
    context = {
        "product": product,
        "discount": discount * 100,
        "final_price": final_price,
    }

    quantity = 0
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)

        for cart_item in cart_items:
            quantity += cart_item.quantity

    context["cart_quantity"] = quantity

    return render(request, 'base/product.html', context)


def cart(request, product_id):
    user = request.user

    if user is not None and user.is_authenticated:
        try:
            cart_item = CartItem.objects.get(user=user, product_id=product_id)

            if cart_item:
                cart_item.quantity += 1
                cart_item.save()

        except CartItem.DoesNotExist:
            product = Product.objects.get(id=product_id)
            cart_item = CartItem(user=user, product=product)
            cart_item.save()

    return redirect('base-product', id=product_id)
