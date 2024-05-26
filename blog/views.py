#blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post



def home(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    context = {
        'posts': posts,
    }
    return render(request, 'home.html', context)


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Assign the logged-in user directly
            post.save()
            return redirect('home')  # Redirect back to the homepage after creating the post
    else:
        form = PostForm()
    context = {'form': form}  # Create context dictionary with the form
    return render(request, 'create_post.html', context)

