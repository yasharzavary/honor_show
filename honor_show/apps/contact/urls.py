from django.urls import path
import apps.contact.views as view

urlpatterns = [
    path('', view.cont, name='contact'),
]
