from django.urls import path
from . import views
from .views import AddCatView,CategoryView

urlpatterns = [
path('',views.gallery,name='gallery'),
path('photo/<slug:slug>/',views.photo,name='photo'),
path('add_photo/',views.add_photo,name='add_photo'),
path('add_category/',AddCatView.as_view(),name='add_category'),
path('search',views.search,name='search'),
path('search_auto',views.search_auto,name='search_auto'),
path('category/<int:id>/',CategoryView,name='categories'),

]