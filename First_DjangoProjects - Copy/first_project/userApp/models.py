from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.  #there is no 1-1 relationship in models so we impose primary as unique 
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)#to which user
    age = models.IntegerField(null=True)
    image = models.ImageField(default='default.jpeg',upload_to = 'profile_pics')

    def __str__(self):
        return str(self.user.username)

