from django.db import models

# Create your models here.

from django.db import models

class Sale(models.Model):
    date = models.DateField()
    store_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    units_sold = models.IntegerField()
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    total_revenue = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        db_table = "sales_fact"
    
    def __str__(self):
        return f"{self.product_name} - {self.store_name}"
