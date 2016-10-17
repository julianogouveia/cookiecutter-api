from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^{{ cookiecutter.app_name }}/', include('apps.{{ cookiecutter.app_name }}.urls')),
]
