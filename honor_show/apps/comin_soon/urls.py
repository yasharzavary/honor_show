from django.urls import path
import apps.coming_soon.views as view

urlpatterns = [
    path('', view.come_soon, name="coming_soon")
]