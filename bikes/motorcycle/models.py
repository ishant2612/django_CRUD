from django.db import models

class Motorcycle(models.Model):
    id = models.AutoField(primary_key=True,default = "N/A")
    brand = models.CharField(max_length=100,default="N/A")
    model = models.CharField(max_length=100,default="N/A")
    year = models.PositiveIntegerField(default=0)
    max_speed = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.brand} {self.model}"
