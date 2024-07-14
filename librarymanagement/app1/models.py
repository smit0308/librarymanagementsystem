from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class librarian(models.Model):
    name=models.CharField(max_length=30)
    
class reader(models.Model):  # Capitalize the model name for consistency
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    full_name = models.CharField(max_length=150, null=True)  # New field for full name
    contact = models.CharField(max_length=15, null=True)  # New field for contact
    
    def __str__(self):
        return self.first_name 