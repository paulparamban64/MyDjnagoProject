from django.urls import path
from .views import post,post_page,edit_post

urlpatterns = [
    path("",post),
    path("<int:id>",post_page),
    path("edit/<int:id>/",edit_post)
]