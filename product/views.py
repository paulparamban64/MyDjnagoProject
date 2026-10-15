
from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm

# Create your views here.
def product(request):
#  data = ["This is the post about Java",
#  "This is the post about Javascript",
#  "This is the post about HTML",
#    "This is the post about CSS",
#  "This is the post about Python",
#  "This is the post about Django"]

  #data = Product.objects.all()

  if request.method == "GET":
    form = ProductForm()
    data = Product.objects.all()
    return render(request,template_name="product.html",context ={"username":request.user})
  elif request.method == 'PRODUCT':
    form = ProductForm(request.Product)
    if form.is_valid():
      form.save()
      return redirect("/products/")