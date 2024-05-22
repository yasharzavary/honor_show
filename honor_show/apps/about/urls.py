from django.urls import path
import apps.about.views as view



urlpatterns = [
    path('', view.abo, name='about'),
]
