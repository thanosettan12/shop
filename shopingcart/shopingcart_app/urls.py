from django.urls import path

app_name = 'shopingcart_app'

from shopingcart_app import views

urlpatterns = [

    path('', views.allprodcat, name='allprodcat'),
    path('home/<slug:c_slug>/', views.allprodcat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proddetail, name='prodcatedetail')
]
