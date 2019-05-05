
from django.shortcuts import render,redirect,get_object_or_404

from meetup.services.userservice import *


def home(request):
    if request.method == 'GET':
        home_view = generate_home_view(request)
        print(home_view['past_meetups'])
        return render(request, 'template/home.html', {'same_city_users':home_view['profiles'],'meetups':home_view['past_meetups']})

def profile(request):
    if request.method == 'POST' :
        process_profile_view(request)
        return redirect('home')
    else :
        forms = generate_profile_view(request)
        return render(request, 'template/profile.html', forms)

def event_by_id(request,event_id):
    #Push to service layer
    event = get_object_or_404(Event,id=uuid.UUID(event_id))
    host = event.host.first()
    location = event.location.first()
    guests = event.guest.all()
    return render(request, 'template/event.html', {'event':event,'host':host,'location':location,'guests':guests})


