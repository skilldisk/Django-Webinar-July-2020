from django.shortcuts import render
from .models import ProductModel

# Create your views here.
def home(request):
    webinar = " Django : Python web framework "
    content = {'webinar':webinar}
    return render(request, 'home.html', content)

def productslist(request):
    products = ProductModel.objects.all()
    content = {'products' : products}
    return render(request,'products.html',content)