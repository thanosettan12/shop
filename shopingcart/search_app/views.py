from django.shortcuts import render, redirect
from shopingcart_app.models import Product
from django.db.models import Q


def search_result(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q', '')
        products = Product.objects.all().filter(Q(name__contains=query) | Q(disc__contains=query))
    return render(request, 'search.html', dict(query=query, products=products))
