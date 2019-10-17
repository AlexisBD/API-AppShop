from rest_framework import routers, serializers, viewsets
from apps.inventories.models import Inventory
from apps.products.serializers import ProductSerializers


class InventorySerializers(serializers.ModelSerializer):
    productName = serializers.ReadOnlyField(source = 'product.name')
    productDesc = serializers.ReadOnlyField(source = 'product.description')
    #productImage= serializers.ReadOnlyField(source = 'product.image')
    class Meta:
        model = Inventory    
        fields = ('id','product', 'user','quantity', 'price', 'tax','productName', 'productDesc' )
