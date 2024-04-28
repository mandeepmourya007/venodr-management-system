from django.shortcuts import render
from rest_framework import generics
from purchase_order.models import PurchaseOrder
from purchase_order.serializers import PurchaseOrderSerializer
# Create your views here.

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    def get_queryset(self):
        vendor = self.request.query_params("vendor")
        if vendor:
            return self.queryset.filter(vendor__name=vendor)
        return 
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer