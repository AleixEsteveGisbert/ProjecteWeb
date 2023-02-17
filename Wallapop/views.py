from django.shortcuts import render
from .models import Ad


# Create your views here.

# List of ads
def ads_list_view(request):
    ads = Ad.objects.all()
    context = {
        'ads_objects': ads,
    }
    return render(request, 'index.html', context)
