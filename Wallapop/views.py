from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authtoken.models import Token

from .forms import RegisterForm, LoginForm, AdForm
from .models import Ad, Comment, UserInfo
from .serializers import AdSerializer, UserSerializer, CommentSerializer, UserInfoSerializer


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permissions_classes = []

    def perform_create(self, serializer):
        serializer.save(id_ad_user_id=self.request.user.id)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permissions_classes = []


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects
    serializer_class = UserSerializer
    permission_classes = []




def index(request):
    return render(request, 'index.html')


def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            token = Token.objects.create(user=user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def ad_new(request):
    form = AdForm()
    return render(request, 'ad_new.html', {'form': form})


def logout(request):
    return render(request, 'logout.html')

def get_profile(request, user_id):
    return render(request, 'profile.html')

def get_ad(request, ad_id):
    return render(request, 'ad_show.html')
