from django.contrib import admin
from django.urls import path
from .import views 

urlpatterns = [
path('login/', views.loginPage, name="login"),
path('logout/', views.logoutUser, name="logout"),

    path('admin/', admin.site.urls),

]