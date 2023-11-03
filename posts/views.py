from django.shortcuts import render, redirect
from .models import Post
from django.http import JsonResponse


# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "posts/index.html", context)


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {"post": post}
    return JsonResponse(context)
