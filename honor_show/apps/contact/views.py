from django.shortcuts import render

def cont(req):
    return render(req, 'contact/index.html')

