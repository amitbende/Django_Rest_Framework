
from rest_framework import serializers
from .models import Employee

def Multiple_of_1000(value):
    if value % 1000 != 0:
        serializers.ValidationError('Value should be multiple of 1000')
    return value


class EmployeeSerializer(serializers.ModelSerializer):
    sal = serializers.FloatField(validators=[Multiple_of_1000])
    class Meta:
        model = Employee
        fields = '__all__'

    def validate_sal(self, value):
        if value < 10000:
            raise serializers.ValidationError('salary should be less than 10000')
        return value

    def validate(self, data):
        email = data.get('email')
        if email.endswith('gmail.com') != True:
            raise serializers.ValidationError('domain should be remain gmail.com only')
        return data


























    # eid = serializers.IntegerField()
    # name = serializers.CharField(max_length=100)
    # company = serializers.CharField(max_length=100)
    # address = serializers.CharField(max_length=100)
    # sal = serializers.FloatField()
    # email = serializers.EmailField()

    # def create(self, validated_data):
    #     return Employee.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.eid = validated_data.get('eid', instance.eid)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.company = validated_data.get('company', instance.company)
    #     instance.address = validated_data.get('address', instance.address)
    #     instance.sal = validated_data.get('sal', instance.sal)
    #     instance.email = validated_data.get('email', instance.email)

    #     instance.save()
    #     return instance

