from audioop import reverse
from email.mime import image
import imp
from tkinter import S
from unicodedata import name
from django.db.models import Q
from django.shortcuts import redirect, render,get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm
from photo.forms import PhotoForm,CatForm
from .models import Category,Photo
from django.views.generic import CreateView

from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def gallery(request):
    category= request.GET.get('category')
    
    if category == None:
        
       photos = Photo.objects.all()
        

    else:  
        photos = Photo.objects.filter(category__name=category)
    categories = Category.objects.all()
    
    cat_menu=Category.objects.all()


    

  
  
  
    return render(request,'photos/gallery.html',{'categories':categories,'photos':photos,'cat_menu':cat_menu})


    



def CategoryView(request,id):
    category_post = Photo.objects.filter(category=id)
    
        


   
    


    return render(request,'photos/categories.html',{'category_post':category_post})



def categories(request):
    return {
        'categories':Category.objects.all()
    }
    
    


    
def photo(request,slug):
    photo = Photo.objects.get(slug=slug)
    


    return render(request,'photos/photo.html',{'photo':photo,})

def search(request):
    if request.method == 'GET':
        searched = request.GET['searched']
        photos = Photo.objects.filter(
            
            Q(category__name__icontains=searched) |
            Q(name__icontains=searched)    |
            Q(desc__icontains=searched)
            )  
        return render(request,'photos/search.html',{'searched':searched,'photos':photos})


    else:   

     return render(request,'photos/search.html')


def search_auto(request):
    if 'term' in request.GET:
        qs = Category.objects.filter(name__icontains=request.GET.get('term'))
        titles = list()
        for category in qs:
            titles.append(category.name)
            

        return JsonResponse(titles,safe=False)    
 
    return render(request,'photos/search.html')


@login_required(login_url='login')
def add_photo(request):
    form = PhotoForm
    if request.method == 'POST':
        form = PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
     

    else:
        form = PhotoForm



    return render(request,'photos/add_photo.html',{'form':form})


class AddCatView(CreateView):
    model = Category
    template_name = 'photos/add_category.html'
    form_class = CatForm
    success_url = reverse_lazy('gallery')



    

    


        