from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate

from .forms import LoginForm, AdForm, RegisterForm, AddComment, EditProfileUser, EditProfileUserInfo
from .models import Ad, Comment, UserInfo

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

    if request.method == 'POST':
        form = AddComment(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.id_comment_user = request.user
            c.id_comment_ad = ad
            c.save()
            return redirect(request.path)
    else:
        form = AddComment()

    context = {
        'ad': ad,
        'comments': comments,
        'form': form,
    }

    return render(request, 'ad_show.html', context)


def comment_edit(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.id_comment_user:
        return redirect('home')
    if request.method == 'POST':
        form = AddComment(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('ad-show', ad_id=comment.id_comment_ad.id)
    else:
        form = AddComment(instance=comment)
    return render(request, 'comment_edit.html', {'form': form})


def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.id_comment_user:
        return redirect('home')
    if request.method == 'POST':
        comment.delete()
        return redirect('ad-show', ad_id=comment.id_comment_ad.id)
    return render(request, 'comment_delete.html', {'comment': comment})


# Login page
def login_form(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
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
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.id_ad_user = request.user
            ad.save()
            return redirect('home')
    else:
        form = AdForm()
    return render(request, 'ad_new.html', {'form': form})


@login_required(login_url='login')
def ad_edit(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    if request.user != ad.id_ad_user:
        return redirect('home')
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AdForm(instance=ad)
    return render(request, 'ad_edit.html', {'form': form, 'ad': ad})


@login_required(login_url='login')
def ad_delete(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    if request.user != ad.id_ad_user:
        return redirect('home')
    if request.method == 'POST':
        ad.delete()
        return redirect('home')
    return render(request, 'ad_delete.html', {'ad': ad})


@login_required(login_url='login')
def edit_profile(request):
    userinfo = request.user.userinfo

    if request.method == 'POST':
        form = EditProfileUser(user=request.user, data=request.POST)
        form1 = EditProfileUserInfo(request.POST, request.FILES, instance=userinfo)

        if form.is_valid() & form1.is_valid():
            form.save()
            form1.save()
            return redirect('login')
    else:
        form = EditProfileUser(user=request.user)
        form1 = EditProfileUserInfo(instance=userinfo)

    return render(request, 'profile_edit.html', {'form': form, 'form1': form1})


def get_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    userinfo = get_object_or_404(UserInfo, user=user)
    ads = user.ad_set.all()

    context = {
        'userP': user,
        'userinfo': userinfo,
        'ads': ads
    }

    return render(request, 'profile.html', context)


def get_userAds(request):
    ads = request.user.ad_set.all()
    return render(request, 'userAds.html', {'ads': ads})
