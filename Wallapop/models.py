from django.db import models

# Create your models here.
# Class Ads
class Ads(models.Model):
    product_name = models.TextField()
    price = models.TextField()

    def __str__(self):
        return self.product_name + ' - ' + self.price