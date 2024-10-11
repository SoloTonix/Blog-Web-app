from django.urls import path 
from .views import *

urlpatterns = [
    path('register/', Register, name='Register'),
    path('login/', Login, name='Login'),
    path('logout/', Logout, name='Logout'),
]

