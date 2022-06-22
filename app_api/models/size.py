from django.db import models

class Size(models.Model):
    size = models.CharField(max_length=50)

    def __str__(self):
        return f'size: {self.size}'