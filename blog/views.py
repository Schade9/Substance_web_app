from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Post, Reply
from .forms import CreatePostForm, PostUpdateForm, ReplyForm
 
@login_required
def index(request):
    posts = Post.objects.all().order_by('-date_posted')
    context = {
        'posts': posts,
    }
    return render(request, "index.html", context)

@login_required
def post_detail(request, pk):
    form = ReplyForm(request.POST or None)
    user = request.user
    replies = Reply.objects.filter(sender=user).order_by('-reply_date')
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.sender = request.user
            form.instance.post = post
            form.save()
            return redirect("index")
    context = {
        'post': post,
        'replies': replies,
        'form': form,
    }
    return render(request, "post_detail.html", context)

@login_required
def create_post(request):
    form = CreatePostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('index')
    else:
        form = CreatePostForm(instance=request.user)

    context = {
        'form': form
    }
    return render(request, "create_post.html", context)

@login_required
def my_posts(request):
    user = request.user
    posts = Post.objects.filter(author=user).order_by('-date_posted')

    context = {
        'posts': posts
    }
    return render(request, "my_posts.html", context)

@login_required
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        if request.method == 'POST':
            form = PostUpdateForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.instance.author = request.user
                form.save()
                return redirect('my_posts')
        else:
            form = PostUpdateForm(instance=post)
        context = {
            'form': form
        }
        return render(request, 'edit_post.html', context)
    else:
        return redirect('page_404')

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        if request.method == "POST":
            post.delete()
            return redirect('my_posts')
        context = {
            'post': post
        }
        return render(request, "delete_post.html", context)
    else:
        return redirect('page_404')

@login_required
def page_404(request):
    return render(request, "404.html", {})

def logout_view(request):
    logout(request)
    return redirect('login')