from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
 
class UserProfiles(models.Model):
     user = models.OneToOneField(User,primary_key=True,blank=False,null=False, on_delete=models.CASCADE)
     dispalay_name = models.CharField(max_length=30,blank=True,null=True)
     address = models.CharField(max_length=100,null=True,blank=True)
     city = models.CharField(max_length=50,null=True,blank=True)
     phone_number = models.IntegerField(blank=True,null=True)

     def __str__(self):
         return self.user

class Product(models.Model):
    product_name = models.CharField(max_length=150,blank=False,null=False,verbose_name='product')
    date_added = models.DateTimeField(default=timezone.now)
    product_description = models.TextField(blank=False,null=False)
    product_price = models.FloatField(blank=False,null=False)
    product_image = models.CharField(max_length=500,null=True,blank=True)
    discount_price = models.FloatField(blank=True,null=True)

    def __str__(self):
        return self.product_name

class Blog(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=150,null=False,blank=False)
    time_created = models.DateTimeField(default=timezone.now)
    body = models.TextField(blank=False,null=False)
    featured_image = models.CharField(max_length=500,null=True,blank=True)
    likes = models.ManyToManyField(User,blank=True, related_name='likes')

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Blog',on_delete=models.CASCADE)
    comment_author = models.CharField(max_length=30,blank=False)
    comment_body = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.comment_author
