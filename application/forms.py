from django import forms


from .models import Post


class PostForm(forms.ModelForm):
    content_of_article = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = ['title', 'content_of_article', 'author']