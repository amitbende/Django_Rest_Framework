from platform import processor
from .models import Laptop
from rest_framework import serializers

class LaptopSerializer(serializers.Serializer):
    laptop_id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    brand = serializers.CharField(max_length=50)
    model = serializers.CharField(max_length=50)
    processer = serializers.CharField(max_length=50)
    price = serializers.FloatField()

    def create(self, validated_data):
        return Laptop.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.laptop_id = validated_data.get('laptop_id', instance.laptop_id)
        instance.name = validated_data.get('name', instance.name)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.model = validated_data.get('model', instance.model)
        instance.processer = validated_data.get('processer', instance.processer)
        instance.price = validated_data.get('price', instance.price)

        instance.save()
        return instance
    

