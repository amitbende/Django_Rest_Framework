from .models import Employee, Project
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    employee_project = ProjectSerializer(read_only=True, many=True)
    class Meta:
        model = Employee
        fields = '__all__'

