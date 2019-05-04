from django.conf.urls import url
from . import views

urlpatterns = [
    url('profile/', views.profile, name='profile'),
]