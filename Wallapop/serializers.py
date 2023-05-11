from django.contrib.auth.models import User
from .models import Ad
from rest_framework import serializers




class AdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ad
        fields = ['product_name', 'description', 'price', 'image']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']