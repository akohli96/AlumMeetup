"""config URL Configuration
"""
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^meetup/',include('meetup.urls', namespace='meetup')),
]
