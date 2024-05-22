from django.shortcuts import render

def will_make(req):
    return render(req, 'will_make/will_make.html')
