from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, "index.html")
def portfolio(request):
    return render(request, "portfolio.html")
def contact(request):
    return render(request,"contact.html")

def service(request):
    product = Producto.objects.all()
    return render(request, "service.html", {'product': product})
