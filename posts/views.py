from django.shortcuts import render
from .models import Post

def home_view(request):
    posts =  Post.objects.all()
    print("dónde están los postssss", posts)
    return render(request, 'posts/home.html', {'posts': posts})

def post_create_view(request):
    return render(request, 'posts/post_create.html')