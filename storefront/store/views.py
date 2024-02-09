from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'store/home.html'  # Assuming 'home.html' is your template name

