#blog/forms.py
from django import forms
from .models import Post, Comment


#___________________________________________________________PostForm
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'img', 'content',]
        

#___________________________________________________________CommentForm
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

    def save(self, user, post, commit=True):
        comment = super().save(commit=False)
        comment.user = user
        comment.post = post

        if commit:
            comment.save()
        return comment