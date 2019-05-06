from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'profile/$', views.profile, name='profile'),
    url(r'home/$', views.home, name='home'),
    url(r'event/(?P<event_id>[0-9A-Fa-f-]+)/$', views.event_by_id, name='event_by_id'),
    url(r'^invite/$', views.invite, name='invite'),
    url(r'^notification/$', views.notification, name='notifcation'),
    url(r'^login/$', auth_views.login, {'template_name': 'template/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]