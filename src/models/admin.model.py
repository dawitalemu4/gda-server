from django.db import models

class Admin(models.Model):
    email = models.CharField(blank=False)
    password = models.CharField(blank=False)