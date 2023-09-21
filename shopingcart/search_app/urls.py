from django.urls import path


app_name = 'search_app'

from .import views

urlpatterns = [

    path('', views.search_result, name='search_result')

]
