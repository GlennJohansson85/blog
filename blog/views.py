from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import PostForm, CommentForm
from .models import Post, Comment


def home(request):
    '''
    Fetches all published posts along with their comments and renders the home page.
    '''
    posts_with_comments = []
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    for post in posts:
        comments = post.comments.all()
        posts_with_comments.append({'post': post, 'comments': comments})
    
    context = {
        'posts_with_comments': posts_with_comments,
        'user': request.user, 
    }
    return render(request, "home.html", context)


@login_required
def create_post(request):
    '''
    Handles the form submission for creating a new post.
    '''
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


def post_detail(request, post_id):
    '''
    Displaying the details of a specific post along with its comments.
    '''
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
        'comment_form': comment_form,
        'user': request.user,
    }
    return render(request, 'post_detail.html', context)


@login_required
def delete_post_confirmation(request, post_id):
    '''
    Displaying the delete post confirmation page.
    '''
    post = get_object_or_404(Post, id=post_id)
    context = {'post': post}
    return render(request, 'delete_post_confirmation.html', context)


@login_required
def delete_post(request, post_id):
    '''
    Function for deleting a post.
    '''
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.user or request.user.is_admin:
        post.delete()
        return redirect('home')
    else:
        return HttpResponseForbidden("You are not authorized to delete this post.")


@login_required
def delete_comment(request, comment_id):
    '''
    Function for deleting a comment.
    '''
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.user or request.user.is_admin:
        comment.delete()
        return redirect('post_detail', post_id=comment.post.id)
    else:
        return HttpResponseForbidden("You are not authorized to delete this comment.")