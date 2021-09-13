# Models file that creates that gives form to the database
# Brand
# Product

from django.db import models
from django.core.validators import MaxValueValidator


class Brand(models.Model):
    brand_name = models.CharField(max_length=500)

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    sku = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(999999999999999)])
    product_name = models.CharField(max_length=500)
    product_price = models.DecimalField(max_digits=50, decimal_places=2)
    product_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    times_searched_anonymous = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.product_name + ' (' + self.product_brand.brand_name + ')' + ' - $' + str(self.product_price)
