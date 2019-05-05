
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from meetup.services.userservice import *
from meetup.services.eventservice import UserFilter,EventForm,invite_send


@login_required
def home(request):
    if request.method == 'GET':
        home_view = generate_home_view(request)
        return render(request, 'template/home.html', {'same_city_users':home_view['profiles'],'meetups':home_view['past_meetups']})

@login_required
def profile(request):
    if request.method == 'POST' :
        process_profile_view(request)
        return redirect('home')
    else :
        forms = generate_profile_view(request)
        return render(request, 'template/profile.html', forms)

def event(request):
    event_form = EventForm()
    if request.method == 'GET':
        #push to service
        user_list = Profile.objects.all()
        user_filter = UserFilter(request.GET, queryset=user_list)
        return render(request, 'template/invite.html', {'filter': user_filter,'event_form':event_form})
    else:
        selected_users=request.POST.getlist('user[]')
        invite_send(request.user,selected_users,request.POST['date'])        
        return redirect('home')
    

@login_required
def event_by_id(request,event_id):
    #Push to service layer
    event = get_object_or_404(Event,id=uuid.UUID(event_id))
    host = event.host.first()
    location = event.location.first()
    guests = event.guest.all()
    return render(request, 'template/event.html', {'event':event,'host':host,'location':location,'guests':guests})


