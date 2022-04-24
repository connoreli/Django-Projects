from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    products = ['Cherries', 'Apples', 'Watermelons', 'Oranges', 'Strawberries', 'Pears']
    context = {
        'products': products,
    }
    return render(request, 'home.html', context)
