"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from firstApp import views as att_views
from django.contrib.auth import views as auth_views
from userApp.views import Profile,loginpage,Profile_user
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path ('hello/',att_views.about,name='hello'),
    path('att/', include('firstApp.urls')),
    #path('login/',auth_views.LoginView.as_view(template_name ="userApp/login.html"),name='Login'),
    path('login/',loginpage,name='Login'),
    path('accounts/profile/',Profile,name='profile'),
    path('logout/',auth_views.LogoutView.as_view(template_name ="userApp/logout.html"),name='Logout'),
    path('profile/',Profile,name='Profile'),
    path('profile/<int:id1>',Profile_user,name='profile_user'),
    path('user/', include('userApp.urls')),
    path('blog/', include('blog.urls')),
    path('api-auth/',include('rest_framework.urls'))
]
urlpatterns = urlpatterns+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
