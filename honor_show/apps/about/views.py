from django.shortcuts import render
from django.conf import settings


def abo(req):
    contex = {
        'media_url':settings.MEDIA_URL,
        'pic_name': 'about_personal.jpg',
    }
    return render(req, 'about/index.html', contex)