from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.transactions.models import Transaction
#from Products.serializers import ProductsSerializers


class TransactionsList(APIView):
    pass

class TransactionsDetail(APIView):
    pass
