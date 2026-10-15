from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.TextField()
    description = models.TextField(max_length=255)
    price = models.IntegerField()
    
    def __str__(self):
        return self.product_name

# Create your models here.
