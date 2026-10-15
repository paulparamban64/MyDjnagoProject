#from django.http import HttpResponse

#from django.shortcuts import render

#def home(request):
#     return render(request,template_name="home.html", {"username":request.user})
#def about(request):
   # return render(request,template_name="about.html", {"username":request.user})

from django.shortcuts import render
#from django.contrib.auth.forms import UserCreationForm

# Create your views here.
#def register_user(request):
 # form = UserCreationForm()
 # return render(request,"register.html",{"form":form})
def home(request):
  return render(request,"home.html",{"username":request.user})

def about(request):
  return render(request,"about.html",{"username":request.user})