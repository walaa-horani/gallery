from django.urls import path
from . import views
from .views import RegisterForm
urlpatterns = [
    path('register/',RegisterForm.as_view(),name='register'),
    
]