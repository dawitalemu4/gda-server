from django.db import models

class sale_clothes_model(models.Model):

    CATEGORIES = {
        "CT": "Clothing, Top",
        "CT": "Clothing, Bottom",
        "CO": "Clothing, Other",
        "A": "Accessories",
        "O": "Other" 
    }
    SIZES = {
        "XXS": "Extra Extra Small",
        "XS": "Extra Small",
        "S": "Small",
        "M": "Medium",
        "L": "Large",
        "XL": "Extra Large",
        "XXL": "Extra Extra Large",
        "OS": "One Size"
    }
    GENDERS = {
        "M": "Male",
        "F": "Female",
        "U": "Unisex"
    }
        
    title = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=False)
    category = models.CharField(max_length=255, blank=False, choices=CATEGORIES)
    size = models.CharField(max_length=255, blank=False, choices=SIZES)
    measurements = models.CharField(max_length=255, blank=False)
    gender = models.CharField(max_length=255, blank=False, choices=GENDERS)
    price = models.IntegerField(blank=False)
    notes = models.CharField(max_length=255)
    thumbnail = models.CharField(max_length=255, blank=False)
    gallery = models.CharField(max_length=255, blank=False)

    def validate(self):
        if not self.title or len(self.title) > 255:
            return False
        elif not self.description or len(self.description) > 255:
            return False
        elif not self.category or len(self.category) > 255 or self.category not in self.CATEGORIES:
            return False
        elif not self.size or len(self.size) > 255 or self.size not in self.SIZES:
            return False
        elif not self.measurements or len(self.measurements) > 255:
            return False
        elif not self.gender or len(self.gender) > 255 or self.gender not in self.GENDERS:
            return False
        elif not self.price:
            return False
        elif len(self.notes) > 255:
            return False
        elif not self.thumbnail or len(self.thumbnail) > 255:
            return False
        elif not self.gallery or len(self.gallery) > 255:
            return False
        else:
            return True