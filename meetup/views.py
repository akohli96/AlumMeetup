
from django.shortcuts import render,redirect

from meetup.services.userservice import *


def profile(request):
    if request.method == 'POST' :
        process_profile_view(request)
        return redirect('template/home.html')
    else :
        forms = generate_profile_view(request)
        return render(request, 'template/profile.html', forms)


