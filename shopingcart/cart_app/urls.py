from django.urls import path

app_name = 'cart_app'

from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('ful_remove/<int:product_id>/', views.ful_remove, name='ful_remove'),
]
