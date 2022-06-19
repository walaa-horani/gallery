from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL,blank=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(null=False,blank=False, upload_to='images')
    slug= models.SlugField(blank=True,null=True)
    desc = models.TextField()

    def save(self,*args,**kwargs):
        if self.slug is not None:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)
        

    def __str__(self):
        return self.desc       