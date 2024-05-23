from django.shortcuts import render
from apps.one_image.models import image
from django.conf import settings


def all(req):
    context = {
        'trophies': image.objects.all(),
        'media_url': settings.MEDIA_URL,
    }
    return render(req, 'all_in_one/all.html', context)
