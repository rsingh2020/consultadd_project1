from django.db import models

class Candidate(models.Model):
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    Email_Id= models.CharField(max_length=30)
from django.db import models

# Create your models here.
