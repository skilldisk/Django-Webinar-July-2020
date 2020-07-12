from django.db import models

# Create your models here.
class ProductModel(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

