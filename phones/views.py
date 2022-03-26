from django.shortcuts import render, redirect
from phones.models import Phone
from django.http import HttpResponse

def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    sorting = request.GET.get('sort')
    if sorting == 'name':
        phones = sorted(Phone.objects.all(), key=lambda phone: phone.name)
    elif sorting == 'min_price':
        phones = sorted(Phone.objects.all(), key=lambda phone: phone.price)
    elif sorting == 'max_price':
        phones = sorted(Phone.objects.all(), key=lambda phone: phone.price, reverse=True)
    else:
        phones = Phone.objects.all()
    context = {
        'phones': phones
    }
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    product = Phone.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, template, context)

