from .models import Employee, Requester, Riders
from rest_framework import serializers


class EmpoyeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'password', 'phone']
    # name = serializers.CharField(max_length=30)
    # email = serializers.EmailField()
    # password = serializers.CharField(max_length=30)
    # phone = serializers.CharField(max_length=30)

    # def create(self, validated_data):
    #     print("create called here")
    #     return Employee.objects.create(**validated_data)
    # 
    # def update(self, employee, validated_data):
    #     new_employee = Employee.objects.create(**validated_data)
    #     new_employee.id = employee.id
    #     new_employee.save()
    #     print("new3EmployeeWWE ", new_employee.id, new_employee.name)
    #     return new_employee


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=30)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)


class RequesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requester
        fields = ['id', 'fromLocation', 'toLocation', 'dateTime', 'flexibleTimings', 'numberOfAssets', 'assetType',
                  'assetSensitivity', 'whomToDeliver', 'status']


class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Riders
        fields = ['id', 'fromLocation', 'toLocation', 'dateTime', 'flexibleTimings', 'numberOfAssets',
                  'status', 'travelMedium', 'acceptedPersonDetails']
