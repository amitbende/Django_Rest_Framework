from django.urls import path
from . import views

urlpatterns = [
    path('lv/', views.LaptopDetails.as_view()),
    path('li/<int:id>/', views.LaptopInfo.as_view())
]