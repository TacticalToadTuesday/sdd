from django.db import models
from django.contrib.auth.models import User
from django.apps import apps

# Create your models here.

class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey relationship with the User model
    result = models.CharField(max_length=9999999)  # Field to store the result with a maximum length
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the created_at field on object creation

    class Meta:
        app_label = 'authentication'  # Set the app_label for this model to 'authentication'
