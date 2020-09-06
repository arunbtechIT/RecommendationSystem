"""recommend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [
    path('',include('home.urls')),
    path('reg', include('home.urls')),
    path('register', include('home.urls')),
    path('Login',include('home.urls')),
    path('admin/', admin.site.urls),path('register',include('home.urls')),
   # path('user_history',include('home.urls')),
    path('search',include('home.urls')),
    path('reverse', include('home.urls')),
    path('recomended',include('home.urls')),
    path('loginpage',include('home.urls')),
    path('signuppage', include('home.urls')),
    path('logout', include('home.urls')),

]
