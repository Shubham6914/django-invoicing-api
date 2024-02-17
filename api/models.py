from django.db import models


class Invoice(models.Model):
   date = models.DateField()
   customer_name = models.CharField(max_length=90)
   
   def __str__(self) :
      return f"{self.date} - {self.customer_name}"
   
   
class InvoiceDetails(models.Model):
   invoice = models.ForeignKey(Invoice,related_name='details', on_delete=models.CASCADE)
   description = models.CharField(max_length=240)
   quantity = models.PositiveIntegerField(default=0)
   unit_price = models.DecimalField(max_digits=10,decimal_places=2)
   price = models.DecimalField(max_digits=10,decimal_places=2)
   
   
   def __str__(self):
      return f"{self.description} - {self.quantity}"