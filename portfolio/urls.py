from django.urls import path
from .views import HomeView, AboutView, ProjectView, TechStackView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('projects/', ProjectView.as_view(), name='project'),
    path('tect-stack/', TechStackView.as_view(), name='tech-stack'),
    path('contact/', ContactView.as_view(), name='contact')
]