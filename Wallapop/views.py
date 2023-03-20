from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate

from .forms import LoginForm, NewAdForm, RegisterForm
from .models import Ad, Comment

from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

# List of ads
def ads_list_view(request):
    ads = Ad.objects.all()
    context = {
        'ads_objects': ads,
    }
    return render(request, 'index.html', context)


# Info of an ad
def get_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    comments = ad.comment_set.all()

    context = {
        'ad': ad,
        'comments': comments,
    }
    return render(request, 'ad_show.html', context)


# Login page
def login_form(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            usuario = authenticate(request, username=form.cleaned_data['username'],
                                   password=form.cleaned_data['password'])
            if usuario is not None:
                login(request, usuario)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register_form(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required(login_url='login')
def ad_new(request):
    if request.method == 'POST':
        form = NewAdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.id_ad_user = request.user
            ad.save()
            return redirect('home')
    else:
        form = NewAdForm()
    return render(request, 'ad_new.html', {'form': form})


def user_profile(request):
    return render(request, 'user_profile.html')