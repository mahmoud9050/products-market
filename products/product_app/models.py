
from django.db import models
from django.db.models.fields import DecimalField
from django.db.models.fields.files import ImageField

# Create your models here.

class Category(models.Model):
    name =models.CharField(max_length=20)
    def __str__(self) :
        return self.name


class Product(models.Model):

    status_product= [
        ('Available','Available'),
        ('Discount','Discount'),
        ('Sold','Sold'),

    ]   
    titel =models.CharField(max_length=100)
    company =models.CharField(max_length=100,null=True, blank=True)
    photo_product =ImageField(upload_to='photos', null=True, blank=True )
    photo_company =ImageField(upload_to='photos', null=True, blank=True )
    quantity =models.IntegerField(null=True, blank=True)
    price = models.DecimalField (max_digits=10 , decimal_places=2 ,null=True, blank=True)
    discount = models.DecimalField (max_digits=10 , decimal_places=2 ,null=True, blank=True)
    discount_for =models.IntegerField(null=True, blank=True)
    total = models.DecimalField (max_digits=10 , decimal_places=2 ,null=True, blank=True)
    active =models.BooleanField(default=True )
    status =models.CharField(max_length=100,choices=status_product,null=True, blank=True )
    category =models.ForeignKey(Category,on_delete=models.PROTECT,null=True, blank=True)
    def __str__(self) :
        return self.titel
