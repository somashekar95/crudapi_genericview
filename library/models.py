from django.db import models

# Create your models here.
class book(models.Model):
    title=models.CharField(max_length=100,blank=True)
    author=models.CharField(max_length=100,blank=True)
    publisher=models.CharField(max_length=100,blank=True)
    date=models.DateTimeField(auto_now_add=True)
def __str__(self):
    return self.title
