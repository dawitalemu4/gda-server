from django.db import models

class sale_clothes(models.Model):
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
    title = models.CharField(blank=False)
    description = models.CharField(blank=False)
    category = models.CharField(blank=False, choices=CATEGORIES)
    size = models.CharField(blank=False, choices=SIZES)
    measurements = models.CharField(blank=False)
    gender = models.CharField(blank=False, choices=GENDERS)
    notes = models.CharField()
    thumbnail = models.CharField(blank=False)
    gallery = models.CharField(blank=False)