from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserCreationForm, CustomUserChangeForm


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(user)
            return redirect('posts:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })


@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'posts:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accoutns/login.html', {
        'form': form,
    })


@require_POST
def logout(request):
    auth_logout(request)
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


@login_required
@require_http_methods(["GET", "POST"])
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instnce=request.user)
        if form.is_valid():
            user = form.save()
            return redirect('accoutns:profile', user.name)
    else:
        form = CustomUserChangeForm(request.user)


@login_required
@require_http_methods(["GET", "POST"])
def change_password(request, user_pk):
    if request.method=="POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('accounts:profile', user.name)
    else:
        form = PasswordChangeForm()
    return render(request, 'accounts/change_password.html', {
        'form': form,
    })


@login_required
def delete(request):
    pass


def profile(request, username):
    pass


def follow(request, user_pk):
    pass


def followers(request, username):
    pass


def following(request, username):
    pass
