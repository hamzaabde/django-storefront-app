from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='base-home'),
    path('login/', views.login, name='base-login'),
    path('logout/', views.logout, name='base-logout'),
    path('register/', views.register, name='base-register'),
    path('product/<int:id>/', views.product, name='base-product'),
    path('cart/<int:product_id>/', views.cart, name='base-cart'),
]
