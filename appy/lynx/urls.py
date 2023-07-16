from django.urls import path
from . import views
# list of all our routes and each one is connected to a view
urlpatterns = [
    path('', views.index, name=''),
    path('dashboard', views.dashboard, name='dashboard'),
    path('login', views.my_login, name='login'),
    path('profile', views.profile_management, name='profile_management'),
    path('register', views.register, name='register'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('delete-account', views.delete_account, name='delete_account'),
]
