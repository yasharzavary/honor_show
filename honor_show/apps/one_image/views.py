from django.shortcuts import render
from .models import Honor, Person
from django.shortcuts import render
from django.conf import settings

def index(req):
    pass


def all(req):
    context = {
        'who_have': Person.objects.all()[0],
        'trophies': Honor.objects.all(),
        'media_url': settings.MEDIA_URL,
    }
    return render(req, 'one_image/all.html', context)
