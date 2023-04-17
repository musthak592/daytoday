from django.shortcuts import render, get_object_or_404
from .models import Product,Category
# Create your views here.
def shop(request):
    obj=Category.objects.all()
    return render(request,'index.html',{'obj':obj})
def clients(request, c_slug=None):
    c_page = None
    products_list = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.filter(category=c_page, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)
    return render(request,'clients.html',{'obj':products_list})
def ProCatDetail(request,c_slug,product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
            raise e
    return render(request,'product.html',{'product':product})

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')