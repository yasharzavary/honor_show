from django.shortcuts import render


def all(req):
    return render(req, 'all_in_one/all.html')
