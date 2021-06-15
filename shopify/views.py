from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact
from math import ceil
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def home(request):
    return render(request,'shopify/layout.html')
def index(request):
    # products=Product.objects.all()
    # #print(products)
    # n=len(products)
    # nslider=n//4 +ceil(n/4)-(n//4)
    # #params={'no_of_slides':nslider,'range':range(1,nslider),'product':products}
    # allProds=[[products,range(1,nslider),nslider],
    #            [products,range(1,nslider),nslider]]
    # params={'allProds':allProds}
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}

    return render(request,'shopify/index2.html',params)
def about(request):
    return render(request,'shopify/about.html')
def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele +'\n'


    # return string
    return str1
import json
def contact(request):
    if request.method=="POST":
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        #print(name,email,phone,desc)
        mydict={'email':email,
                   'name':name,
                   'phone':phone,
                   'description':desc}
        #aList = json.dumps(jsonString)
        mydict2=json.dumps(mydict, indent=4)
        MYLIST=[name,email,phone,desc]
        print(listToString(MYLIST))
        m_list=listToString(MYLIST)

        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        send_mail(name,mydict2,email,['b17101072.namraabid@gmail.com'],    fail_silently=False)
        print(send_mail)
    return render(request,'shopify/contact.html')
def tracker(request):
    return render(request,'shopify/tracker.html')
def search(request):
    return render(request,'shopify/search.html')
def productView(request,myid):
    product=Product.objects.filter(id=myid)
    print(product)
    return render(request,'shopify/prodView.html',{'product':product[0]})
def checkout(request):
    return render(request,'shopify/checkout.html')
