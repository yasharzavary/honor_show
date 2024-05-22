from django.urls import path
import apps.will_make.views as view

urlpatterns=[
    path('', view.will_make, name='will_make')
]