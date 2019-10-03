from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib.auth.models import User
from django.utils import timezone

from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.products.models import Product
from apps.inventories.models import Inventory
from apps.products.serializers import ProductSerializers
from apps.inventories.serializers import InventorySerializers
from apps.transactions.models import Transaction


class ProductsList(APIView):
    def get(self, request, format=None):
        queryset = Product.objects.all()
        serializer = ProductSerializers(queryset, many=True)        
        return Response(serializer.data)
    
    def post(self, request, format=None):
        rol = request.user.is_superuser        
        if rol == True:
            serializerProduct = ProductSerializers(data = request.data)            
            if serializerProduct.is_valid():                
                serializerProduct.save()                                
                datas = serializerProduct.data                 
                ##########  POST FOR INVENTORY #############                               
                postInventory = Inventory.objects.create(
                    user_id     = request.user.id,
                    product_id  = datas['id'],
                    quantity    = request.data['quantity'],
                    price       = request.data['price'],
                    tax         = request.data['tax']                    
                )
                postInventory.save()
                ##########  POST FOR TRANSACTIONS #############                             
                Transaction.objects.create(
                    inventory_id    = postInventory.id,
                    dates           = timezone.now(),
                    types           = 1,
                    quantity        = postInventory.quantity,
                    description     = "Se agrego " + request.data['quantity'] + " "+datas['name']
                )                
                return Response(datas)
            return Response(serializerProduct.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response("No eres administrador")

class ProductsDetail(APIView):
    def get_object(self, id):
        try:            
            return Product.objects.get(pk=id) 
        except Product.DoesNotExist: 
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = ProductSerializers(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        rol = request.user.is_superuser
        if rol == True:
            Product.objects.get(pk=id)
            return Response("Delete Success")
        else:
            return Response("No eres administrador")
    
    def put(self, request, id, format=None):        
        rol = request.user.is_superuser
        example = self.get_object(id)
        if rol == True:
            if example != False:
                serializer = ProductSerializers(example, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    datas = serializer.data
                    return Response(datas)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response("No eres administrador")
