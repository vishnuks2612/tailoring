from django.db import models
from django.urls import reverse


# Create your models here.
class user_login(models.Model):
    uname = models.CharField(max_length=100)
    passwd = models.CharField(max_length=25)
    u_type = models.CharField(max_length=10)


class user_details(models.Model):
    user_id = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=200)
    addr = models.CharField(max_length=500)
    pin = models.IntegerField()
    contact = models.IntegerField()
    email = models.CharField(max_length=25 )

    def __str__(self):
        return self.fname
    

class Category(models.Model):
    name=models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('user_home', args=[self.slug])

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.CharField(max_length=500)
    image = models.ImageField(upload_to='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    

    def __str__(self):
        return self.product_name


class Feedback(models.Model):
    user = models.CharField(max_length=50, default='')
    message = models.CharField(max_length=500)
   

    def __str__(self):
        return self.user


class purchase(models.Model):
    size = models.CharField(max_length=25, default='')
    card = models.CharField(max_length=25)
    number = models.CharField(max_length=25)
    email = models.CharField(max_length=50, default='')
    mobile = models.CharField(max_length=12, default='')
    address = models.CharField(max_length=200, default='')
    cvv = models.CharField(max_length=25)
    product = models.ForeignKey(Product, on_delete = models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.card














