from django.shortcuts import render
from blog.models import Post
# Create your views here.


def all_blogs(request):
    posts = Post.objects.all()
    return render(request , 'blog/all_blogs.html',{'posts': posts})