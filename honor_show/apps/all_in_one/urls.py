from django.urls import path
import apps.all_in_one.views as view

urlpatterns = [
    path('', view.all, name='all_in_one'),
]
