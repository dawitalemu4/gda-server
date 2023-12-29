from django.db import models

class admin_model(models.Model):
    
    name = models.CharField(max_length=255, blank=False)
    password = models.CharField(max_length=255, blank=False)

    def validate(self):
        if not self.name or len(self.name) > 255:
            return False
        elif not self.password or len(self.password) > 255:
            return False
        else:
            return True