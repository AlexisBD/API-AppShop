from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.sales.models import Sale
from apps.sales.serializers import SaleSerializers
from apps.inventories.models import Inventory
#from apps.inventories.views import In
from apps.inventories.serializers import InventorySerializers

# Sales = Sal
# Inventory = Inv
class Operaciones ():
    def __init__(self, Inventory, Sale):
        self.Inv = Inventory
        self.Sal = Sale

    def residuo (self):
        return int(self.Inv['quantity']) - int(self.Sal['quantity'])

    def subtotal (self):
        total = int(self.Sal['quantity']) * float(self.Inv['price'])
        descuento = (total * self.Sal['discount'])/100
        return total - descuento

    def total (self):
        iva = (self.subtotal() * float(self.Inv['tax']))/100
        return self.subtotal + iva

    def res (self):
        resultado = []
        resultado.append(self.residuo)
        resultado.append(self.subtotal)
        resultado.append(self.total)
        return resultado