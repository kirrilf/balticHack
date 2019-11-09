
from django.urls import path

from .views import *

urlpatterns = [
    path('upload/', ImageViewSet.as_view(), name='upload'),
]

