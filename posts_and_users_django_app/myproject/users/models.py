from django.db import models

# Create your models here.

class User(models.Model):
  first_name = models.CharField(max_length=100)
  second_name = models.CharField(max_length=100)
  email =  models.EmailField(max_length=254)
  password = models.CharField(max_length=100)

  def __str__(self) -> str:
    return self.first_name
