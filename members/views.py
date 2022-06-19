from django.shortcuts import render
from django.views.generic import CreateView
from django.views import generic
from .forms import SignUpForm
from django.urls import reverse_lazy

# Create your views here.
class RegisterForm(generic.CreateView):
    form_class= SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')