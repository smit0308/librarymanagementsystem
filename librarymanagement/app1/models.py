from django.db import models

# Create your models here.
class librarian(models.Model):
    name=models.CharField(max_length=30)
    