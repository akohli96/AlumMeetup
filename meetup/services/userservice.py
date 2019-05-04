from meetup.repository.models import *
from django.forms import inlineformset_factory
from django import forms

class LocationForm(forms.Form):
    city = forms.CharField(max_length=50)
    country = forms.CharField(max_length=50)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','first_name','last_name','username')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user','location',)

def generate_profile_view(request):
    user = User.objects.get(id=request.user.id)
    userForm = UserForm(instance=user)
    profileForm = ProfileForm(instance=Profile.objects.get(user=user))
    locationForm=None
    if(user.profile.location):
        locationForm = LocationForm({'city':user.profile.location.city,'country':user.profile.location.country})
    else:
        locationForm = LocationForm()
    return {'user_form':userForm,'profile_form':profileForm,'location_form':locationForm}

def process_profile_view(request):
    #Push these three to a function
    user = User.objects.get(id=request.user.id)
    userForm = UserForm(request.POST,instance=user)
    profileForm = ProfileForm(request.POST,instance=Profile.objects.get(user=request.user.id))
    if userForm.is_valid() and profileForm.is_valid():
        nebulousLocation,created = Location.objects.get_or_create(city=request.POST.get('city'),country=request.POST.get('country'))
        profile = profileForm.save(commit=False)
        profile.location = nebulousLocation
        user = userForm.save(commit=False)
        user.save()
        profile.save()
        #Maybe to DB layer
    else:
        raise Exception("Form not valid")   

def generate_home_view(request):
    curr_user = User.objects.get(id=request.user.id)
    profiles =Profile.objects.exclude(user=curr_user).filter(location=curr_user.profile.location).order_by('user__last_login')[0:5]
    events_eligble = Event.objects.filter(location=curr_user.profile.location).filter(public=True)
    past_meetups = events_eligble.filter(date__lte=timezone.now().today())[0:5]
    return {'profiles':profiles,'past_meetups':past_meetups}
    #Profile.objects.exclude(user=u).filter(location=u.profile.location)