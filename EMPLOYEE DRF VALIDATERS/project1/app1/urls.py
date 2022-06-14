from django.urls import path
from . import views

urlpatterns = [
    path('emp/', views.EmployeeDetails.as_view()),
    path('emp/<int:id>/', views.EmployeeInfo.as_view())
]