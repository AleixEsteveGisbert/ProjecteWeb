from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate


from .forms import Register, LoginForm
from .models import Ad

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
def get_ad(request, adid):
    obj = get_object_or_404(Ad, id=adid)

    context = {
        'ad': obj,
    }
    return render(request, 'ad_show.html', context)

# Login page
def login_form(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            usuario = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if usuario is not None:
                login(request, usuario)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register_form(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = Register()
    return render(request, 'register.html', {'form': form})