from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# Create your views here.
from .serializers import EmpoyeeSerializer, UserSerializer, RequesterSerializer, RiderSerializer
from .models import Employee, Requester, Riders
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from test1.enums import *
from django.core.paginator import Paginator

@csrf_exempt
def employeeListView(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmpoyeeSerializer(employees, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmpoyeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, safe=False)


@csrf_exempt
def employeeDetailView(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return HttpResponse(status=404)
    print(employee)
    if request.method == 'GET':
        serializer = EmpoyeeSerializer(employee)
        return JsonResponse(serializer.data)
    if request.method == 'DELETE':
        employee.delete()
        return HttpResponse(status=204)
    if request.method == 'PUT':
        jsonData = JSONParser().parse(request)
        print("pu reqeuest", jsonData)
        serializer = EmpoyeeSerializer(employee, data=jsonData)
        # print("serializer_data ",serializer.data)
        if serializer.is_valid():
            serializer.save()
            print("reached_here1 ", serializer.data)
            return JsonResponse(serializer.data, safe=False)
        print("4error")
        return JsonResponse(serializer.errors, safe=False)
    return HttpResponse(401)


def userListView(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def requesterListView(request):
    print("hello")
    if request.method == 'GET':
        # requests = Requester.objects.all()
        filters = {}
        if request.GET.get('status'):
            filters['status'] = request.GET['status']
        if request.GET['assetType']:
            filters['assetType'] = request.GET['assetType']
        requests = Requester.objects.filter(**filters)
        if request.GET['sortDateTime']:
            if request.GET['sortDateTime'] == 'DESC':
                requests = requests.order_by('dateTime')
            else:
                requests = requests.order_by('-dateTime')
        if request.GET.get('page'):
            page = request.GET['page']
            p = Paginator(requests,2)
            requests = p.page(page)
        serializer = RequesterSerializer(requests, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data['status'] = "PENDING"
        serializer = RequesterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, safe=False)


@csrf_exempt
def riderListView(request):
    print("hello")
    if request.method == 'GET':
        requests = Riders.objects.all()
        serializer = RiderSerializer(requests, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data['status'] = "NOTAPPLIED"
        serializer = RiderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, safe=False)
