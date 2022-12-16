from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def loginPage(request):

    if request.method == 'POST':
        #Get the post parameters
         username = request.POST('username')
        password = request.POST('password')

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