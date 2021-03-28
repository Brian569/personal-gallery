from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name

    def save_travel(self):
        self.save()
    

class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = CloudinaryField('image')
    description = models.TextField(max_length=500, blank=False)

    def __str__(self):
        return self.description

    def save_photo(self):
        self.save()
    
# 