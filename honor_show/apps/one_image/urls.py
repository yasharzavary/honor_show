from django.urls import path
import apps.one_image.views as view


urlpatterns = [
    path('', view.index, name='one-image'),
]