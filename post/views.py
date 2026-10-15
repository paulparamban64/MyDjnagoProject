
from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.
def post(request):
#  data = [
# "This is the post about Java",
#  "This is the post about Javascript",
#  "This is the post about HTML",
#  "This is the post about CSS",
#  "This is the post about Python",
#  "This is the post about Django"]

  if request.method == "GET":
    form = PostForm()
    data = Post.objects.all()
    return render(request,template_name="post.html", context={"data":data,"form":form,"username":request.user})
      #context ={"data":data,"form":form,"username":request.user})
  elif request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      form.save()
    return redirect("/post/")

def post_page(request,id):
  if request.method == "GET":
    post_obj = Post.objects.get(post_id = id)
    return render(request,"post_page.html",{"post":post_obj})
  elif request.method == "POST":
    post_obj = Post.objects.get(post_id = id)
    post_obj.delete()
    return redirect("/post/")

def edit_post(request,id):
  post_obj = get_object_or_404(Post,post_id = id)
 
  if request.method == "GET":
    return render(request,"edit_post.html",{"post":post_obj})
 
  elif request.method == "POST":
    title = request.POST.get("post_title")
    description = request.POST.get("description")
    content = request.POST.get("content")

    if not title or not content:
        return render(request,"edit_post.html",{"post":post_obj})
    
    post_obj.post_title = title
    post_obj.description = description
    post_obj.content = content

    post_obj.save()

    return redirect("/post/")
        