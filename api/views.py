from django.shortcuts import render
from .models import Invoice, InvoiceDetails
from .serializers import InvoiceSerializer,InvoiceDetailsSerialzer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages
from django.shortcuts import get_object_or_404



class InvoiceAPIview(APIView):
   def get_object(self, pk):
        return get_object_or_404(Invoice, pk=pk)
     
   def get(self,request):
      invoice = Invoice.objects.all()
      serializer = InvoiceDetailsSerialzer(invoice, many=True)
      return Response(serializer.data)
   
   def post(self,request, format=None):
      serializer = InvoiceSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response({
            "msg" : "Invoice Created Successfully",
            "status" : "Success",
            "candidate" : serializer.data,}, status= status.HTTP_201_CREATED)
      return Response(serializer.errors)
   
   def put(self,request,pk,format=None):
      invoice_detail = self.get_object(pk)
      serializer = InvoiceSerializer(invoice_detail, data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response({
            "msg" : "Invoice Updated Successfully",
            "status" : "Success",
            "candidate" : serializer.data,}, status= status.HTTP_201_CREATED)
      return Response(serializer.errors)
   
   def delete(self,request,pk,format=None):
      invoice = self.get_object(pk)
      invoice.delete()
      return Response({
            "msg" : "Invoice Deleted Successfully",
            "status" : "Success",}, status= status.HTTP_200_OK)
      



class InvoiceDetailAPIview(APIView):
   def get_object(self, pk):
        return get_object_or_404(Invoice, pk=pk)
     
   def get(self,request):
      invoice = InvoiceDetails.objects.all()
      serializer = InvoiceDetailsSerialzer(invoice, many=True)
      return Response(serializer.data)
   
   def post(self,request, format=None):
      serializer = InvoiceDetailsSerialzer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response({
            "msg" : "Invoice Details Created Successfully",
            "status" : "Success",
            "candidate" : serializer.data,}, status= status.HTTP_201_CREATED)
      return Response(serializer.errors)
   
   # def put(self,request,pk,format=None):
   #    invoice_detail = self.get_object(pk)
   #    serializer = InvoiceDetailsSerialzer(invoice_detail, data=request.data)
   #    print(serializer)
   #    if serializer.is_valid():
   #       serializer.save()
   #       return Response({
   #          "msg" : "Invoice Details Updated Successfully",
   #          "status" : "Success",
   #          "candidate" : serializer.data,}, status= status.HTTP_201_CREATED)
   #    return Response(serializer.errors)
   def put(self, request, pk):
        try:
            invoice_detail = InvoiceDetails.objects.get(pk=pk)
        except InvoiceDetails.DoesNotExist:
            return Response({"error": "Invoice detail not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = InvoiceDetailsSerialzer(invoice_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
               "msg" : "Invoice Details Updated Successfully",
               "status" : "Success",
               "candidate" : serializer.data,}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
   def delete(self, request, pk, format=None):
        invoice_detail = self.get_object(pk)
        invoice_detail.delete()
        return Response({
            "msg": "Invoice Details Deleted Successfully",
            "status": "Success"
        }, status=status.HTTP_200_OK)