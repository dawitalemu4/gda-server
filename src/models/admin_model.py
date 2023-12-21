from django.db import models

class admin(models.Model):
    email = models.CharField(blank=False)
    password = models.CharField(blank=False)