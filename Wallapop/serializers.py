from django.contrib.auth.models import User
from .models import Ad, UserInfo, Comment
from rest_framework import serializers


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['user', 'description', 'avatar']


class UserSerializer(serializers.ModelSerializer):
    userinfo = UserInfoSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'userinfo']


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)
    user_id = serializers.SerializerMethodField(read_only=True)
    id_comment_user = UserSerializer(read_only=True)
    ad = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'id_comment_ad', 'id_comment_user', 'username', 'user_id', 'ad', 'comment', 'created_at']

    def get_username(self, obj):
        return obj.id_comment_user.username

    def get_user_id(self, obj):
        return obj.id_comment_user.id


class AdSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    id_ad_user = UserSerializer(read_only=True)

    class Meta:
        model = Ad
        fields = ['id', 'product_name', 'description', 'price', 'image', 'id_ad_user', 'comments']
