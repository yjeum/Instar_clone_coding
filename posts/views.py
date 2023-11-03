from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.views.decorators.http import (
    require_safe,
    require_http_methods,
    require_POST,
)
from django.http import JsonResponse
from .forms import PostForm, CommentForm
from .models import Post, Comment


# Create your views here.
@require_http_methods(["GET", "POST"])
def index(request):
    if request.method == "GET":
        print("들어옴")
        posts = get_list_or_404(Post)
        comments = get_list_or_404(Comment)
        context = {
            "posts": posts,
            "comments": comments,
        }
        return render(request, "posts/index.html", context)
    elif request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            form.save()
            return redirect("posts:index.html")
        else:
            form = PostForm()
        context = {
            "form": form,
        }
        return render(request, "posts/create.html", context)


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm()
    comments = post.comment_set.all()
    context = {
        "post": post,
        "comment_form": comment_form,
        "comments": comments,
    }
    return JsonResponse(context)
