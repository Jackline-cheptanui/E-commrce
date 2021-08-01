from django.shortcuts import render
from.models import Product

def index(request):
    Product_objects= Product.objects.all()
    # search code
    item_name=request .GET .get('item_name')
    if item_name != '' and item_name is not None:
        Product_objects=Product_objects.filter(title__icontains=item_name) 
#  paginator
        paginator = paginator(Product_objects,4)
        page=request.GET.get('page')
        Product_objects= paginator.get_page(page)
    return render(request,'commerce/index.html',{'product_objects':Product_objects})

def detail(request,id):
    product_object=Product.objects.get(id=id)
    return render(request,"commerce/detail.html",{'product_object':'Product_object'})