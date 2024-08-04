from multiprocessing import context
from pyexpat import model
from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView
from .models import About, Project, Expereince, Education, Contact
# Create your views here.

########################### work on 404 page

class HomeView(ListView):
    model = About
    template_name = 'portfolio/index.html'
    context_object_name = 'about' # assign a name to use in a for loop in template

    def get_context_data(self, **kwargs): # this function allows me to list several objects in models while using a single template
        context = super().get_context_data(**kwargs) 
        context['projects'] = Project.objects.all() # This line connect the model you want to add to the List view
        return context
    
class AboutView(ListView):
    model = About
    template_name = 'portfolio/about.html'
    context_object_name = 'about' # assign a name to use in a for loop in template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expereince'] = Expereince.objects.all() # This line connect the model you want to add to the List view
        context["education"] = Education.objects.all() # This line connect the model you want to add to the List view
        return context

class ProjectView(ListView):
    model = Project
    template_name = 'portfolio/project.html'
    context_object_name = 'projects'

class TechStackView(TemplateView):
    template_name = 'portfolio/tech_stack.html'

class ContactView(CreateView):
    model = Contact
    template_name = 'portfolio/contact.html'