from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    productId=models.CharField(primary_key=True,max_length=10,default="False")
    productName=models.CharField(max_length=50,default='')
    productDiscription=models.CharField(max_length=600,default='')
    productImage=models.ImageField(null="False",upload_to='static/Images')
    productCompany=models.CharField(max_length=50,default='')
    price=models.FloatField()
    productCategory=models.CharField(max_length=50,default='')
    def __str__(self):
        return self.productName

class Customer(models.Model):
    link=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    customerImage=models.ImageField(null="False", upload_to='static/Images')
    review=models.CharField(null="True", max_length=500)
