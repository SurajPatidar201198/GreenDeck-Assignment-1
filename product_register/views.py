import csv,io
from django.shortcuts import render,redirect
from .forms import ProductForm
from .models import Product
# Create your views here.

def product_list(request):
    context = {'product_list': Product.objects.all()}
    return render(request,"product_register/product_list.html",context)

def product_form(request,id=0):
    if request.method == "GET":
        if id==0:
            form = ProductForm()
        else:
            product = Product.objects.get(pk=id)
            form = ProductForm(instance = product)
        return render(request,"product_register/product_form.html",{'form':form})
    else:
        if id == 0 :
            form = ProductForm(request.POST)
        else:
            product = Product.objects.get(pk=id)
            form = ProductForm(request.POST,instance = product)
        if form.is_valid():
            form.save()
        return redirect('/product/list')

def product_delete(request,id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect('/product/list')

def product_upload(request):
    template="product_register/product_upload.html"
    context= {'product_list':Product.objects.all()}
    if request.method == "GET":
        return render(request,template)
    
    csv_file = request.FILES['file']
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=','):
        _, created = Product.objects.update_or_create(
            name = column[0],
            brand_name = column[1],
            regular_price_value = column[2],
            offer_price_value = column[3],
            currency = column[4],
            classification_l1 = column[5],
            classification_l2 = column[6],
            classification_l3 = column[7],
            classification_l4 = column[8],
            image_url = column[9]
        )      
    return redirect('/product/list')

