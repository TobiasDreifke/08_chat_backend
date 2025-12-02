from django.db import models

# Create your models here.

class Chat(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    message = models.CharField(max_length = 30, blank = True, default = "")
    created_at = models.DateField(auto_now=False, auto_now_add=True)