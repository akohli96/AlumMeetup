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