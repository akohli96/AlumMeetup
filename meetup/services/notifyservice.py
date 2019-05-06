from notifications.signals import notify
from notifications.models import *
from meetup.models import *
#<actor> <verb> <target> <created>

def get_all_notifications(user):
    return user.notifications.all()

def delete(id,recepient):
    notification = Notification.objects.get(recipient=recepient,id=id)
    notification.delete()

def invite(event):
    profiles = event.guest.all()
    users=[]
    for profile in profiles:
        p=profile
        users.append(User.objects.get(pk=p.user.pk)) #Investigate why model queryset is not returning appropriate result
    return notify.send(event.host.first().user,recipient=users,actor=event.host.first().user,verb='invited you',target=event, description='invitation to event')