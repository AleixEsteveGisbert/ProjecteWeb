from django.contrib.auth.models import User
from .models import Ad, UserInfo, Comment
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Comment
        fields = ['comment', 'created_at', 'author']


class AdSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Ad
        fields = ['product_name', 'description', 'price', 'image', 'comments']


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['user', 'description', 'avatar']
