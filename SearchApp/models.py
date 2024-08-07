from django.db import models

class CarDetails(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name