from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class contacts(models.Model):
    """Create contact model"""
    name = models.CharField(max_length=255)
    mobile_no = PhoneNumberField()
    email = models.EmailField(unique=True,max_length=255)
    address = models.TextField(max_length=1000)

    def __str__(self):
        return self.email
