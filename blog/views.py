#blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from .models import Post

#___________________________________________________________home
def home(request):
    # Fetch all posts along with their comments
    posts_with_comments = []
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    for post in posts:
        comments = post.comments.all()
        posts_with_comments.append({'post': post, 'comments': comments})
    
    context = {
        'posts_with_comments': posts_with_comments,
    }
    return render(request, "home.html", context)


#___________________________________________________________create_post
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form    = PostForm()
    context     = {
        'form': form
    }
    
    return render(request, 'create_post.html', context)


#___________________________________________________________post_detail
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            profile = request.user
            comment_form.save(user=profile, post=post)
            return redirect('home')
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(request, 'post_detail.html', context)