from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product
from math import ceil
from django.http import HttpResponse

def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds}
    return render(request, 'index.html', params)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request=='POST':
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('Phone', '')
        desc=request.POST.get('desc ', '')
        print(name,email,phone, desc )
    return render(request, 'contact.html')

def tracker(request):
    return render(request, 'tracker.html')

def search(request):
    return render(request, 'search.html')

def productView(request, myid):
    product=Product.objects.get(id=myid)
    print(product)
    return render(request, "prodview.html",{'pro':product})
def checkout(request):
    return render(request, 'checkout.html')