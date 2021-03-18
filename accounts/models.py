from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Profile(models.Model):
    full_name = models.CharField(max_length=50)
    image = models.ImageField()
    age = models.IntegerField()
    date_join = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    wallet = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=40)

    def __str__(self):
        return self.full_name