from django.urls import path 
from .views import HomePageView, UserManagementView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('users', UserManagementView.as_view(), name='users'),
]