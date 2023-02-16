from django.shortcuts import render

# Create your views here.

# List of ads
def ads_list_view(request):
    ads = Ads.objects.all()
    context = {
        'ads_objects' : ads,
    }
    return render(request, 'index.html', context)