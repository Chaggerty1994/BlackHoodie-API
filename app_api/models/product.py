from operator import truediv
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(validators=[MinValueValidator(0.00), MaxValueValidator(1000.00)])
    category = models.ForeignKey(
        "category", on_delete=models.CASCADE, related_name='products')
    size = models.ForeignKey(
        "size", on_delete=models.CASCADE, related_name='products', default=3)
    image_path = models.ImageField(upload_to='products', height_field=None, 
                                    width_field=None, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.clean_fields()
        super().save(*args, **kwargs)

    @property
    def number_purchased(self):
        """Returns the number of times product shows up on completed orders
        """
        return self.orders.exclude(payment_type=None).count()

    def __str__(self):
        return self.title