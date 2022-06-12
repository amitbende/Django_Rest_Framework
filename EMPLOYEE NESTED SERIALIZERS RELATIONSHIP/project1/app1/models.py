from tkinter import CASCADE
from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField()
    name = models.CharField(max_length=50)
    salary = models.FloatField()

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=50)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_project')

    def __str__(self):
        return self.name


