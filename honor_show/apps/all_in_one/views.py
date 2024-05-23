from django.shortcuts import render
from apps.one_image.models import image

def all(req):
    context = {
        'trophies': image.objects.all(),
    }
    return render(req, 'all_in_one/all.html', context)
