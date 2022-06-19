from django import forms
from .models import Photo,Category 
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User

choices = Category.objects.all().values_list('name','name')

choice_list = []
for item in choices:
    choice_list.append(item)

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('category','name','image','desc')

        widgets = {

            'category': forms.Select(choices=choice_list,   attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control'}),
            

        }


class CatForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'add category'}),

           
            

        }     


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name= forms.CharField(max_length=100)

  


    class Meta:
        model = User
        fields =('username','first_name', 'last_name', 'email','password1','password2',)