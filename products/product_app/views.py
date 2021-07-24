from django.shortcuts import redirect, render ,get_object_or_404
from .models import *
from .forms import ProductForm,CatForm


# Create your views here.
def index(request):

    if request.method == 'POST' :
        add_product = ProductForm(request.POST,request.FILES)
        if add_product.is_valid():
            add_product.save()
        add_category = CatForm(request.POST)
        if add_category.is_valid():
            add_category.save()
        
    context ={
        'products':Product.objects.all(),
        'cat':Category.objects.all(),
        'form': ProductForm(),
        'catf': CatForm(),
        'allproducts':Product.objects.filter(active=True).count(),
        'productsold':Product.objects.filter(status='Sold').count(),
        'productdiscound':Product.objects.filter(status='Discount').count(),
        'productavailble':Product.objects.filter(status='Available').count(),
        
    }
 

    return render (request,'pages/index.html', context)
def products(request):
    search=Product.objects.all()

    titel= None
    if 'search_name' in request.GET:
        titel = request.GET['search_name']
        if titel:
            search= search.filter(titel__icontains=titel)
    context ={
        'products':search,
        'cat':Category.objects.all(),
        'catf': CatForm(),
    }
    return render (request,'pages/product.html', context)
def update(request ,id):
    product_id = Product.objects.get(id=id)
    if request .method == 'POST':
        product_save = ProductForm(request.POST,request.FILES,instance=product_id)
        if product_save.is_valid():
            product_save.save()
            return redirect('/')
    else:
        product_save = ProductForm(instance = product_id)
    context={
        'fo':product_save,
    }
    return render (request,'pages/update.html',context)

def delete(request,id):
    product_delet = get_object_or_404(Product, id=id)
    if request.method == 'POST' :
        product_delet.delete()
        return redirect('/')
    return render (request,'pages/delete.html')
