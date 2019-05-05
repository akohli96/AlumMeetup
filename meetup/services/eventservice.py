import django_filters
from meetup.repository.models import *
from django import forms
from meetup.services.notifyservice import invite


class UserFilter(django_filters.FilterSet):
    user__last_name = django_filters.CharFilter(lookup_expr='icontains')
    user__first_name = django_filters.CharFilter(lookup_expr='icontains')
    year__gt = django_filters.NumberFilter(field_name='year', lookup_expr='year__gt')
    year__lt = django_filters.NumberFilter(field_name='year', lookup_expr='year__lt')
    class Meta:
        model = Profile
        fields = ['user__last_name','user__first_name','school',]

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('date',)

def invite_send(host,particpants_list,date):
    new_event = create_and_save_event(host,particpants_list,date)
    invite(new_event)
    return

def create_and_save_event(host,particpants_list,date):
    event = Event.objects.create(date=date)
    #profiles = Profile.objects.filter(pk__in=particpants_list) Investigate
    event.host.add(host.profile)
    for participant in particpants_list:
        profile = Profile.objects.get(user_id=int(participant))
        event.guest.add(profile)
    event.location.add(host.profile.location)
    event.save()
    return event