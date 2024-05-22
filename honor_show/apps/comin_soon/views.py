from django.shortcuts import render

def come_soon(req):
    return render(req, 'coming_soon/index.html')