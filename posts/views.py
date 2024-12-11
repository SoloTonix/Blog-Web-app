from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages 
from django.contrib.auth.decorators import login_required

# python manage.py runserver
# python manage.py startapp
# python manage.py makemigrations
# python manage.py migrate

# Create your views here.

@login_required
def home(request):
    posts = Post.objects.filter(publish=True).order_by('-created')
    latests = posts[:3]
    context = {'posts':posts, 'latests':latests}
    return render(request, 'posts/home.html', context)

@login_required
def detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.author = request.user
            var.post = post
            var.save()
            context = {'post':post, 'comments':comments, 'form':form}
            return redirect('detail', pk=pk)
    else:
        form = CreateCommentForm()
        context = {'post':post, 'comments':comments, 'form':form}
        return render(request, 'posts/detail.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            if post.publish == True:
                messages.success(request, 'Your story has been successfully created and published .')
            else:
                messages.warning(request, 'Your story has been successfully created but not published yet.')
            return redirect('home')
        else:
            messages.warning(request,'Sorry, something went wrong')
            return redirect('create')
    else:
        form = CreatePostForm()
    context = {'form':form}
    return render(request, 'posts/create.html', context)

def update(request, pk):
    post = Post.objects.get(pk=pk, author=request.user)

    if request.method == 'GET':
        form = CreatePostForm(request.GET or None, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Post has been Updated')
            return redirect('personal')
        else:
            messages.warning(request, 'Sorry, something went wrong')
    else:
        form = CreatePostForm()

    context = {'form':form, 'post':post}
    return render(request, 'posts/update.html', context)

@login_required
def personal(request):
    posts = Post.objects.filter(author=request.user)
    context = {'posts':posts}
    return render(request, 'posts/personal.html', context)

@login_required
def personal_2(request):
    posts = Post.objects.filter(author=request.user)
    context = {'posts':posts}
    return render(request, 'posts/personal_2.html', context)

@login_required
def unpublish(request, pk):
    post = Post.objects.get(pk=pk)
    post.publish = False
    return redirect('personal')

@login_required
def republish(request, pk):
    post = Post.objects.get(pk=pk)
    post.publish = True
    return redirect('personal')

@login_required
def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('personal')
        
        

