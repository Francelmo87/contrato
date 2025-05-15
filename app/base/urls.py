from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from app.base import views as v


app_name = 'base'

urlpatterns = [
    path('',v.home, name = 'home'),
]