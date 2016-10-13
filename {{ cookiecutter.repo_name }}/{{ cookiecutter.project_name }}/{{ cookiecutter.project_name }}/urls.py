from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^{{ cookiecutter.app_name }}/', apps.{{ cookiecutter.project_name }}.urls),
]
