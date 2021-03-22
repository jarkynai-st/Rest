from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    year = models.DateTimeField()
    abbr = models.CharField(max_length=20,unique=True)
    book_file = models.FileField(blank=True)
    price = models.PositiveIntegerField(default=0)
    author = models.ForeignKey('Author',on_delete=models.SET_NULL,null=True,related_name='books')
    sale = models.BooleanField(default=False)
    sale_amount = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    date_birth = models.DateField()
    date_death = models.DateField(blank=True)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Order(models.Model):
    statuses = (
        ('pending','pending'),
        ('finished','finished'),
    )
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,)
    book = models.ForeignKey(Book,on_delete=models.SET_NULL,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=100,null=True)
    quantity = models.PositiveIntegerField()
    status = models.CharField(choices=statuses,max_length=20,default='pending')
    total_sum = models.PositiveIntegerField(default=0)
    payment_type = models.CharField(choices=(
        ('card','card'),
        ('cash','cash'),
    ),max_length=40,default='cash')
    promocode = models.CharField(max_length=5,null=True,blank=True)

    def __str__(self):
        try:
            return f"Заказ с товаром.{self.book.title}"
        except AttributeError:
            return "Книга не найдена!"


    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class Branch(models.Model):
    name = models.CharField(max_length=50)


class Contact(models.Model):
    statuses = (
        ('email','email'),
        ('phone','phone'),
        ('address','address'),
    )
    type = models.CharField(choices=statuses,max_length=40)
    info = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True,related_name='contacts')



