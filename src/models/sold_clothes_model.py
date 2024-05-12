from django.db import models
from django.contrib.postgres.fields import ArrayField

class sold_clothes_model(models.Model):

    CATEGORIES = [
        ("CT", "Clothing, Top"),
        ("CB", "Clothing, Bottom"),
        ("CO", "Clothing, Other"),
        ("A", "Accessories"),
        ("O", "Other")
    ]
    SIZES = [
        ("XXS", "Extra Extra Small"),
        ("XS", "Extra Small"),
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
        ("XL", "Extra Large"),
        ("XXL", "Extra Extra Large"),
        ("OS", "One Size")
    ]
    GENDERS = [
        ("M", "Male"),
        ("F", "Female"),
        ("U", "Unisex")
    ]

    title = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=False)
    category = models.CharField(max_length=255, blank=False, choices=CATEGORIES)
    size = models.CharField(max_length=255, blank=False, choices=SIZES)
    measurements = models.CharField(max_length=255, blank=False)
    gender = models.CharField(max_length=255, blank=False, choices=GENDERS)
    notes = models.CharField(max_length=255)
    thumbnail = models.CharField(max_length=255, blank=False)
    gallery = ArrayField(models.CharField(max_length=2000, blank=False))

    def validate(self):
        if not self.title or len(self.title) > 255:
            return False
        if not self.description or len(self.description) > 255:
            return False
        if not self.category or len(self.category) > 255 or not any(self.category in pair for pair in self.CATEGORIES):
            return False
        if not self.size or len(self.size) > 255 or not any(self.size in pair for pair in self.SIZES):
            return False
        if not self.measurements or len(self.measurements) > 255:
            return False
        if not self.gender or len(self.gender) > 255 or not any(self.gender in pair for pair in self.GENDERS):
            return False
        if len(self.notes) > 255:
            return False
        if not self.thumbnail or len(self.thumbnail) > 255:
            return False
        if not self.gallery or len(self.gallery) > 2000:
            return False

        return True

    class Meta:
        db_table = "sold_clothes"
        verbose_name = "sold_clothes"
        verbose_name_plural = "sold_clothes"