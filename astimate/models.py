from django.db import models
from api.models import Book
# Create your models here.

class Rate(models.Model):
    star = models.PositiveIntegerField()
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='rates')

    def __str__(self):
        return self.book.title


