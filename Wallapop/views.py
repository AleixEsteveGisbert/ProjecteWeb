from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def retrieve_user(request):
    queryset = User.objects.all()  # Set the desired queryset

    try:
        # Retrieve the authorization token from the request headers
        token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[-1]

        # Retrieve the token object
        token_obj = Token.objects.get(key=token)

        # Retrieve the associated user
        user = queryset.get(id=token_obj.user_id)

        # Serialize the user data if needed
        user_serializer = UserSerializer(user)
        serialized_user = user_serializer.data

        # Return the user data as the API response
        return Response(serialized_user, status=status.HTTP_200_OK)

    except Token.DoesNotExist:
        return Response('Invalid token', status=status.HTTP_401_UNAUTHORIZED)

    except User.DoesNotExist:
        return Response('User not found', status=status.HTTP_404_NOT_FOUND)
