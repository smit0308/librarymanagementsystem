from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

# Create your models here.
class librarian(models.Model):
    name=models.CharField(max_length=30)
    
class reader(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)
    address = models.CharField(max_length=100)
    full_name = models.CharField(max_length=150, null=True) 
    contact = models.CharField(max_length=15, null=True) 
    
    def __str__(self):
        return self.first_name 
    
class Booked(models.Model):
    reader = models.ForeignKey(reader, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    allocated_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()

    def save(self, *args, **kwargs):
        self.due_date = self.allocated_date + timedelta(days=30)
        super().save(*args, **kwargs)