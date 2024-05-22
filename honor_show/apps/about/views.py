from django.shortcuts import render

def abo(req):
    return render(req, 'about/index.html')