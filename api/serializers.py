from rest_framework import serializers
from .models import Invoice, InvoiceDetails



class InvoiceSerializer(serializers.ModelSerializer):
   class Meta:
      model = Invoice
      fields = '__all__'
      
      
class InvoiceDetailsSerialzer(serializers.ModelSerializer):
   invoice_date = serializers.DateField(source='invoice.date', read_only=True)
   # This line adds the date field from the related Invoice model
    
   class Meta:
      model = InvoiceDetails
      fields = ['invoice', 'invoice_date', 'description', 'quantity', 'unit_price', 'price']  # Include 'invoice_date' in the fields list
      
      
