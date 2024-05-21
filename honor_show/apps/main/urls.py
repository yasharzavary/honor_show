from django.urls import path
import apps.mian.views as view

urlpatterns = [
    path('', view.index, name='main-index')
]