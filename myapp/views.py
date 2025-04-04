from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Count
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from .models import CustomUser, Post ,ProfileUpdate
from .forms import RegisterForm, PostForm

User = get_user_model()

def post_list(request):
    author_username = request.GET.get('author')
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    if author_username:
        posts = posts.filter(author__username=author_username)

    return render(request, 'post_list.html', {'posts': posts})



@login_required(login_url='/login/')  
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

@login_required(login_url='/login/')
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})



@login_required(login_url='/login/')
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})


@login_required(login_url='/login/')
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user and not request.user.is_superuser:
        return HttpResponseForbidden("You are not allowed to delete this post.")
    post.delete()
    messages.success(request, "Post deleted successfully.")
    return redirect('post_list')



def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            
            user.save()
            login(request, user)  
            # messages.success(request, f"Your registration as has been successful!")  
            return redirect("post_list")  
        else:
            messages.error(request, "Please correct the errors below.") 
    else:
        form = RegisterForm()
    
    return render(request, "register.html", {"form": form})



def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("post_list")  
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")


@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return redirect("login")  


@login_required
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user)

    context = {
        'profile_user': user,
        'posts': posts,
    }


    return render(request, 'user_profile.html', context)

def profile_list(request):
    profiles = ProfileUpdate.objects.all()  # Get all objects
    return render(request, "profiles.html", {"profiles": profiles})  # Pass to template

