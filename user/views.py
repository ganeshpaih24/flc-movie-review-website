from django.shortcuts import render
from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from user.forms import SignupForm,EditProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile


# Create your views here.
def loginPage(request):

    if request.method == 'POST':
        #Get the post parameters
         username = request.POST.get('username')
         password = request.POST.get('password')

     #try:
      #      user = user.objects.get(username=username)
   # except:
     #   messages.error(request, 'user does not exist')
        
         user = authenticate(request,username=username, password=password)

    if user is not None:
            login(request,user)
            messages.success(request, "successfully Logged in")
            return redirect('home')
    else:
            messages.error(request, 'Username or Password does not exist')
            return redirect('home')

    context = {}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Successfully logged out")
    return redirect('home')


def Signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
            return redirect('login.html')
        
	print(form.errors)

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
			return redirect('index')
	else:
		form = EditProfileForm()

	context = {
		'form': form,
	}

	return render(request, 'user/edit_profile.html', context)

