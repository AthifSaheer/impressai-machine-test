from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    
    path('stupid', views.stupid, name='stupid'),
    path('fat', views.fat, name='fat'),
    path('dumb', views.dumb, name='dumb'),
]
