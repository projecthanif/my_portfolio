from django.shortcuts import render
from django.views.generic import ListView
from .models import About, Project
# Create your views here.

########################### work on 404 page

class HomeView(ListView):
    model = About
    template_name = 'portfolio/index.html'
    context_object_name = 'about'

    def get_context_data(self, **kwargs): # this function allows me to list several objects in models
        context = super().get_context_data(**kwargs) # while using a single template
        context['projects'] = Project.objects.all()
        return context