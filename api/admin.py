from django.contrib import admin
from .models import Invoice, InvoiceDetails

@admin.register(Invoice)

class AdminInvoice(admin.ModelAdmin):
   list_display = ['id','date','customer_name']
   

@admin.register(InvoiceDetails)

class AdminInvoiceDetails(admin.ModelAdmin):
   list_display = ['id','invoice','description','quantity','unit_price','price']