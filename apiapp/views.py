from ast import Pass
from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ourusers
from .serializers import ourusersSerialzers

class ourusersLists(APIView):

    def get(self, request):
        ourusersData = ourusers.objects.all()
        serializer = ourusersSerialzers(ourusersData, many = True)
        return Response(serializer.data)

    def post(self):
        Pass
