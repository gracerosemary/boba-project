from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

class Boba(models.Model):
    drink = models.CharField(max_length=64)
    business = models.CharField(max_length=40, default="", help_text="Enter store/cafe name")
    description = models.TextField(default="")
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.drink

    def get_absolute_url(self):
        return reverse('boba_detail', args=[str(self.id)])