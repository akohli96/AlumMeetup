from notifications.signals import notify
from meetup.models import *
#<actor> <verb> <target> <created>

def invite(event):
    profiles = event.guest.all()
    users=[]
    for profile in profiles:
        p=profile
        users.append(User.objects.get(pk=p.user.pk)) #Investigate why model queryset is not returning appropriate result
    return notify.send(event.host.first().user,recipient=users,actor=event.host.first().user,verb='invited you',target=event, description='invitation to event')