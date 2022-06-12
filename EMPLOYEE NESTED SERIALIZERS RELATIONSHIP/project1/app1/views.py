from django.shortcuts import render
from .models import Employee, Project
from .serializers import EmployeeSerializer, ProjectSerializer
from rest_framework import generics

# Create your views here.
class EmployeeDetails(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class Employee_Info(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ProjectDetails(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class Project_Info(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


