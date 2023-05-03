from rest_framework import serializers
from .models import Post, AccessChoices


class PostSerializer(serializers.ModelSerializer):
    access = serializers.ChoiceField(choices=AccessChoices.choices)
    
    class Meta:
        model = Post
        fields = ('id', 'access', 'text', 'created_at', 'posted_by')
        read_only_fields = ('id', 'created_at', 'posted_by')
