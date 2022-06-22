from django.db import models

class OrderProduct(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    product_size = models.ForeignKey("ProductSize", on_delete=models.CASCADE)
