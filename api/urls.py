from django.urls import path,include
from api import views
urlpatterns = [
    path('invoice/',views.InvoiceAPIview.as_view(),name='invoice'),
    path('invoice/<int:pk>/',views.InvoiceAPIview.as_view(),name='select_invoice'),
    path('invoice_detail/',views.InvoiceDetailAPIview.as_view(),name='invoice_detail'),
    path('invoice_detail/<int:pk>/',views.InvoiceDetailAPIview.as_view(),name='select_invoice_detail'),
]
