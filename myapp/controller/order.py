from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import redirect, render

from myapp.models import Order, OrderItem

def index(request):
    orders = Order.objects.filter(user=request.user)
    context = {'orders':orders}
    return render(request,"layout/order.html", context)

def vieworders(request, Tracking_no):
    order = Order.objects.filter(tracking_no=Tracking_no).filter(user=request.user).first()
    orderitems = OrderItem.objects.filter(order=order)
    context = {'order':order, 'orderitems':orderitems}
    return render(request, "layout/vieworder.html", context)