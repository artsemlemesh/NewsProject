from rest_framework import serializers

from .models import Post, Comment, Author

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'title']

