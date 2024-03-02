from django.contrib import admin
from django.urls import include, path

from myapp.views import *

urlpatterns = [
    path('user', UserView.as_view() ),
    path('products', productView.as_view() ),
    path('category', collectionsView.as_view() ),
    path('cart', CartView.as_view() ),
    path('wishlist', WishlistView.as_view() ),
    path('order', OrderView.as_view() ),
]

