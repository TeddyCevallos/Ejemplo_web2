from django.shortcuts import render
from .models import Cliente

# Create your views here.
def index(request):
    return render(request, "index.html")
def portfolio(request):
    return render(request, "portfolio.html")
def contact(request):
    return render(request,"contact.html")
