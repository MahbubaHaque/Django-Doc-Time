from django.urls import path

from users.views import (signup, logout, login, profile)

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('profile/<int:id>/', profile, name='profile')
]