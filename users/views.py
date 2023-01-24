from django.shortcuts import render
from rest_framework.views import APIView
from . import serializers
from . import managers

from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import AllowAny
from . import models
import datetime


# Create your views here.

class UserView(APIView):

    def get(self,request):
        objects = models.User.objects.all()
        serializer = serializers.GetUserSerializer(objects,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)\

    def post(self,request):
        serializer = serializers.GetUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_date=datetime.datetime.now())
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class OneUserView(APIView):

    def get(self,request,pk):
        object = models.User.objects.get(id=pk)
        serializer = serializers.GetUserSerializer(object)
        return Response(serializer.data,status=status.HTTP_200_OK)


class RegisterView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = serializers.RegisterSerializer
