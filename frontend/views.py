from django.shortcuts import render
from django.views import generic

class HomePageView(generic.TemplateView):
    template_name = 'home.html'

class UserManagementView(generic.TemplateView):
    template_name = 'usermanagement.html'
