from django.urls import path
from . import views

urlpatterns = [
path('',views.index,name='index'),
path('reg',views.reg,name='reg'),
path('Login',views.Login,name='Login'),
path('register',views.register,name='register'),
#path('user_history',views.user_history,name='user_history'),
path('recomended',views.recomended,name='recomended'),
path('reverse',views.reverse,name='reverse'),
path('search',views.recomended,name='recomended'),
path('loginpage',views.gotologin,name='gotologin'),
path('signuppage',views.gotosignup,name='gotosignup'),
path('logout',views.logout,name='logout')

]
