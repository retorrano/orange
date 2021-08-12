from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address=models.CharField(max_length=50)
    card_number=models.CharField(max_length=50, unique=True, null=True)
    def __str__(self):
        return self.name