from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import RegisterForm
from .models import Ad


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
def login_page(request):

    return render(request, 'login.html')

# Register page
def register_page(request):

    return render(request, 'register.html')


def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'mymodule/register.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()

                # Login the user
                login(request, user)

                # redirect to accounts page:
                return HttpResponseRedirect('/mymodule/account')

    # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})