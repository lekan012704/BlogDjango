from email import message
from tabnanny import verbose
from django.db import models

# Create your models here.
class Contact(models.Model):

 

    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")

    def __str__(self):
        return self.name

    

