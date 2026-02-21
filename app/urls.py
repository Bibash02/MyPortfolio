from django.urls import path
from .views import portfolio, contact, projects

urlpatterns = [
    path('', portfolio, name='portfolio'),
    path('contact', contact, name='contact'),
    path('projects', projects, name='projects'),
]