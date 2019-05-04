from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'profile/$', views.profile, name='profile'),
    url(r'home/$', views.home, name='home'),
    url(r'event/(?P<event_id>[0-9A-Fa-f-]+)/$', views.event_by_id, name='event_by_id')

]