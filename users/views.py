from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def register_user(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("/user/login")
  else:
    form = UserCreationForm()
  return render(request,"register.html",{"form":form})

def login_user(request):
  if request.method == "POST":
    form = AuthenticationForm(request,data =request.POST)
    if form.is_valid():
      user = authenticate(username=form.cleaned_data["username"],password = form.cleaned_data["password"])
      if user is not None:
        login(request,user)
        return redirect("/")
  else:
    form = AuthenticationForm()
  return render(request,"login.html",{"form":form})


def logout_user(request):
  logout(request)
  return redirect("/")