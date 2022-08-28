from concurrent.futures.process import _python_exit
from itertools import product
from math import ceil
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .models import Contect

# Create your views here.

def index(request):
    product = Product.objects.all()
    n=len(product)

    allprods=[]
    catprods= Product.objects.values('p_category','id')
    cats ={item['p_category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(p_category=cat)
        nSlides=(n//4 + ceil((n//4)-(n/4)))
        allprods.append([prod,range(1,nSlides),nSlides])
    params={'allprod':allprods}

    return render(request,"shop/index.html",params)


def about(request):
    return render(request,"shop/about.html")

def contect(request):
    if request.method=='POST':
        name=request.POST.get('ContectName','')
        email=request.POST.get('ContectEmail','')
        phone=request.POST.get('ContectNumber','')
        desc=request.POST.get('Contectdesc','')
        contect=Contect(name=name,email=email,phone=phone,desc=desc)
        contect.save()
    return  render(request,"shop/Contect.html")

def tracker(request):
    return HttpResponse("Tracker ")

def search(request):
    return HttpResponse("Search ")

def productview(request,myid):
    prod = Product.objects.filter(id=myid)
    return render(request,"shop/productView.html", {'prod':prod[0]})
 
def chekout(request):
    return render(request,"shop/chekout.html")
