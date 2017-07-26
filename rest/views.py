from django.shortcuts import render

from rest_framework import serializers
from rest import models
from rest.rest_serializers import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from rest_framework import status
from rest_framework.response import Response
import json



'''
限制只能get和post, 其他请求就拒绝了
'''
@api_view(['GET', 'POST'])
def saltrun_list(request):

    if request.method == 'GET':
        eventlogs = models.Saltrun.objects.all()
        serializer = SaltrunSerializer(eventlogs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print("request", request.data)
        serializer = SaltrunSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','PUT'])
@csrf_exempt
def saltrun_detail(request, pk):

    try:
        eventlog_obj = models.Saltrun.objects.get(pk=pk)
    except models.Saltrun.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SaltrunSerializer(eventlog_obj)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        print(request)
        data = JSONParser().parse(request)
        serializer = SaltrunSerializer(eventlog_obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        eventlog_obj.delete()
        return HttpResponse(status=204)