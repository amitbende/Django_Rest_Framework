from functools import partial
from django.shortcuts import render
from .models import Laptop
from .serializers import LaptopSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class LaptopDetails(APIView):
    def get(self, request):
        lap = Laptop.objects.all()
        serializer = LaptopSerializer(lap, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LaptopSerializer(data= request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LaptopInfo(APIView):
    def get(self, reuqest, id):
        try:
            lap = Laptop.objects.get(laptop_id = id)
        except Laptop.DoesNotExist:
            msg = {'msg':'Laptop Record Does Not Exist'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = LaptopSerializer(lap)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            lap = Laptop.objects.get(laptop_id = id)
        except Laptop.DoesNotExist:
            msg = {'msg': 'Laptop Record Not Found'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = LaptopSerializer(lap, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        try:
            lap = Laptop.objects.get(laptop_id = id)
        except Laptop.DoesNotExist:
            msg = {'msg': 'Laptop Record Not Fount'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = LaptopSerializer(lap, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            lap = Laptop.objects.get(laptop_id = id)
        except Laptop.DoesNotExist:
            msg = {'msg': 'Laptop Record Not Fount'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        lap.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

