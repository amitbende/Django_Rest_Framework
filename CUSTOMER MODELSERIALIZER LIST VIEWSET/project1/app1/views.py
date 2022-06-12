from functools import partial
from django.shortcuts import render
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

# Create your views here.
class CustomerDetails(viewsets.ViewSet):
    def list(self, request):
        cust = Customer.objects.all()
        serializer = CustomerSerializer(cust, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = CustomerSerializer(data = request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        try:
            cust = Customer.objects.get(cid = pk)
        except Customer.DoesNotExist:
            msg = {'msg':'Customer Record Not Found'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = CustomerSerializer(cust)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk):
        try:
            cust = Customer.objects.get(cid = pk)
        except Customer.DoesNotExist:
            msg = {'msg':'Customer Record Not Found'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = CustomerSerializer(cust, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        try:
            cust = Customer.objects.get(cid = pk)
        except Customer.DoesNotExist:
            msg = {'msg':'Customer Record Not Found'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = CustomerSerializer(cust, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            cust = Customer.objects.get(cid = pk)
        except Customer.DoesNotExist:
            msg = {'msg':'Customer Record Not Found'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        cust.delete()
        msg = {'msg':'Record Delete Successfully!!'}
        return Response(msg, status=status.HTTP_204_NO_CONTENT)




