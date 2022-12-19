from django.urls import path
from .views import Signup,EditProfile
from django.contrib.auth import views as userViews


urlpatterns = [
    path('login/', userViews.LoginView.as_view(template_name='user/login.html'), name='login'),
	path('logout/', userViews.LogoutView.as_view(), name='logout'),
    path('profile/edit', EditProfile, name='edit-profile'),
	path('signup/', Signup, name='signup'),
]