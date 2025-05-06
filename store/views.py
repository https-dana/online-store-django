from django.shortcuts import render

def index(request):
    return render(request, 'store/index.html')

def about(request):
    return render(request, 'store/about.html')

def products(request):
    return render(request, 'store/products.html')

def single_product(request):
    return render(request, 'store/single-product.html')

def contact(request):
    return render(request, 'store/contact.html')
