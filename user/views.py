from django.shortcuts import render,get_object_or_404
from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from user.forms import SignupForm,EditProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.template import loader
from django.http import HttpResponse



def Signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
            return redirect('login')
    else:
        form = SignupForm()

    context = {
        'form': form,
    }

    return render(request, 'user/register.html', context)


@login_required
def EditProfile(request):
    user = request.user.id
    profile = Profile.objects.get(user__id=user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile.picture = form.cleaned_data.get('picture')
            profile.first_name = form.cleaned_data.get('first_name')
            profile.last_name = form.cleaned_data.get('last_name')
            profile.location = form.cleaned_data.get('location')
            profile.url = form.cleaned_data.get('url')
            profile.profile_info = form.cleaned_data.get('profile_info')
            profile.save()
            return redirect('profile',username=profile.user.username)
    else:
        form = EditProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'user/edit_profile.html', context)

def UserProfile(request,username):
    user=get_object_or_404(User,username=username)
    profile=Profile.objects.get(user=user)
    context={
        'profile':profile
    }
    template=loader.get_template('user/user_profile.html')
    return HttpResponse(template.render(context,request))