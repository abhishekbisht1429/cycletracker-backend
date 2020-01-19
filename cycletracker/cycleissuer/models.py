from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.IntegerField(primary_key=True)
    def __str__(self):
        return str(self.username)
    
class Cycle(models.Model):
    qrcode = models.CharField(unique=True, max_length=1000)
    lock = models.BooleanField()
    user = models.OneToOneField(User, on_delete = models.SET_NULL, null = True, blank = True)

