from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.sales.models import Sale
from apps.sales.serializers import SaleSerializers
from apps.inventories.models import Inventory
from apps.sales.operaciones import Operaciones
from apps.inventories.serializers import InventorySerializers


class SalesList(APIView):
    def get(self, request, format=None):
        queryset = Inventory.objects.all()
        serializer = SaleSerializers(queryset, many=True)        
        return Response(serializer.data)


    def post(self, request, format=None):        
        saleInventory = SaleSerializers(data = request.data)  

        print("Request ", request.data)
        productId = int(request.data['product'])
        print("type value", type(productId))
        
        SALES = request.data

        searchIdProduct = Inventory.objects.get(product=2) 
        serializerInventory = InventorySerializers(searchIdProduct)                     
        INVENTORY = serializerInventory.data

        op = Operaciones(INVENTORY, SALES)
        print(op.res())

        
        # quantityInventoryActual = dataInventory['quantity']
        
        # quantitySalesSend = request.data['quantity']
        
        # quantityInventoryActual = int(quantityInventoryActual) - int(quantitySalesSend)
        
        # totalSale = int(quantitySalesSend) * float(dataInventory['price'])
        # print("Total ", totalSale)
        # subTotalSale = totalSale - (totalSale * float(SALES['discount'])/100)
        # print("Subttotal: ", subTotalSale)
        # totalSale = subTotalSale + float(SALES['tax'])

             
        if saleInventory.is_valid():                
            saleInventory.save()                         
            datas = saleInventory.data                                       
            return Response(datas)
        return Response(saleInventory.errors, status = status.HTTP_400_BAD_REQUEST)        

class SalesDetail(APIView):
    def get_object(self, id):
        try:            
            return Sale.objects.get(pk=id) 
        except Inventory.DoesNotExist: 
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = SaleSerializers(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        rol = request.user.is_staff
        if rol == True:
            Inventory.objects.get(pk=id)
            return Response("Delete Success")
        else:
            return Response("No eres administrador")
    
    def put(self, request, id, format=None):        
        rol = request.user.is_staff
        example = self.get_object(id)
        if rol == True:
            if example != False:
                serializer = SaleSerializers(example, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    datas = serializer.data
                    return Response(datas)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response("No eres administrador")
