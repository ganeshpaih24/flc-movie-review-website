from django.urls import path
from .views import EditProfile,Signup
from django.contrib.auth import views as userViews
from user.views import UserProfile

urlpatterns = [
    path('login/', userViews.LoginView.as_view(template_name='user/login.html',next_page='landing'), name='login'),
	path('logout/', userViews.LogoutView.as_view(next_page='landing'), name='logout'),
	path('profile/<username>/', UserProfile, name='profile'),
    path('profile/edit', EditProfile, name='edit-profile'),
	path('signup/', Signup, name='register'),
]