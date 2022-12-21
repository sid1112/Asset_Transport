from datetime import date, datetime
from django.http import JsonResponse, HttpResponse
from .serializers import RequesterSerializer, RiderSerializer
from .models import Requester, Riders
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.core.paginator import Paginator

pageSize = 2


@csrf_exempt
def requesterListView(request):
    if request.method == 'GET':
        filters = {}
        if request.GET.get('status'):
            filters['status'] = request.GET['status']
        if request.GET.get('assetType'):
            filters['assetType'] = request.GET['assetType']
        requests = Requester.objects.filter(**filters)
        if request.GET.get('sortDateTime'):
            if request.GET['sortDateTime'] == 'DESC':
                requests = requests.order_by('dateTime')
            else:
                requests = requests.order_by('-dateTime')
        page = None
        if request.GET.get('page'):
            page = request.GET['page']
            p = Paginator(requests, pageSize)
            requests = p.page(page)
        ##TODO LOOP requests and add EXPIRED status if datetime exceeds
        serializer = RequesterSerializer(requests, many=True)
        return JsonResponse({"data": serializer.data, "page": page}, safe=False)
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


@csrf_exempt
def riderView(request, pk):
    try:
        rider = Riders.objects.get(pk=pk)
    except Riders.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = RiderSerializer(rider)
        return JsonResponse(serializer.data)
    if request.method == 'PUT':
        jsonData = JSONParser().parse(request)
        serializer = RiderSerializer(rider, data=jsonData)
        # print("serializer_data ",serializer.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, safe=False)
    if request.method == 'DELETE':
        rider.delete()
        return HttpResponse(status=204)


@csrf_exempt
def matchedTransportRequestListView(request):
    if request.method == 'GET':
        jsonData = JSONParser().parse(request)
        filters = {}
        if "dateTime" not in jsonData or "toLocation" not in jsonData or "fromLocation" not in jsonData:
            return HttpResponse(400)
        try:
            dateTime = jsonData.get("dateTime")
            format_data = "%d-%m-%Y %H:%M"
            dateTime = datetime.strptime(dateTime, format_data)
            date_inputed, month, year = dateTime.day, dateTime.month, dateTime.year
            filters["dateTime__date"] = date(year, month, date_inputed)
        except:
            raise Exception("input correct date as %d-%m-%Y %H:%M")
        filters["toLocation"] = jsonData.get("toLocation")
        filters["fromLocation"] = jsonData.get("fromLocation")
        filters["status"] = "NOTAPPLIED"
        page = None
        requests = Riders.objects.filter(**filters)
        if request.GET.get('page'):
            page = request.GET['page']
            p = Paginator(requests, pageSize)
            requests = p.page(page)
        serializer = RiderSerializer(requests, many=True)
        return JsonResponse({"data": serializer.data, "page": page}, safe=False)
