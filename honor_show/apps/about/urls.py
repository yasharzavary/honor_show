from django.urls import path
import apps.about.views as view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', view.abo, name='about'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
