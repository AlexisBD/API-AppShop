from rest_framework import routers, serializers, viewsets
from apps.sales.models import Sale


class SaleSerializers(serializers.ModelSerializer):
    productName = serializers.ReadOnlyField(source = 'product.name')
    productName = serializers.ReadOnlyField(source = 'user.username')
    class Meta:
        model = Sale
        fields = ('id', 'quantity', 'discount', 'total', 'dates', 'payment', 'status',
        'product', 'productName', 'user', 'userName')

 