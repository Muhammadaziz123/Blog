from django.shortcuts import render, redirect
from .models import Post
from .forms import *
import random
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            pass
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            pass
    return render(request, 'index/login.html')

def sign_up(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form':form
    }
    return render(request, 'index/sign_up.html',context)

def logout_user(request):
    logout(request)
    return redirect('index')


def index(request):
    search_q = request.GET.get('q','')
    category_q = request.GET.get('category','')
    if 'q' in request.GET:
        posts = Post.objects.filter(title__icontains=search_q).order_by('-id')
    elif 'category' in request.GET:
        posts = Post.objects.filter(category__title=category_q).order_by('-id')
    else:
        posts = Post.objects.all().order_by('-id')
   
    context = {
        'posts':posts,
        'search_q':search_q
    }
    return render(request, 'index/index.html',context)

def post_details(request, pk):
    post = Post.objects.get(id=pk)
    posts = Post.objects.all()
    categories = Category.objects.all()
    recommended_posts = list(posts)
    random.shuffle(recommended_posts)

    context = {
        'post':post,
        'categories':categories,
        'recommended_posts':recommended_posts[:2]
    }
    return render(request, 'index/post_details.html', context)




def post_create(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect("index")
        
    context = {
        'form':form
    }
    return render(request, 'index/post_create.html',context)

def user_posts(request):
    posts = Post.objects.filter(user=request.user).order_by('-id')

    context = {
        'posts':posts,
    }
    return render(request, 'index/user_posts.html', context)


def post_update(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_details", pk=pk)
        
    context = {
        'form':form
    }
    return render(request, 'index/post_update.html', context)

def post_delete(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('index')
    
    context = {
        'post':post
    }
    return render(request, 'index/post_delete.html', context)

def pricing_page(request):
    return render(request, 'index/pricing.html')

def features_page(request):
    return render(request, 'index/features.html')

def faqs_page(request):
    return render(request, 'index/faqs.html')