from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from . import models
from rest_framework.renderers import JSONRenderer
import datetime
from django.db.models.functions import Lower
from django.db.models import Q, CharField
from notifications.views import send_notification
from notifications.models import Notification
from notifications.serializers import SendedNotificationSerializer
from users.models import User


class UserBookView(APIView):

    def get(self,request):
        get_data=request.query_params
        objects = models.UserBook.objects.all()
        if get_data:
            if get_data.get('filter', '')== 'newest':
                objects = objects.order_by('-pk')
            elif get_data.get('filter', '')== 'lowest':
                objects = objects.order_by('price')
            elif get_data.get('filter', '')== 'highest':
                objects = objects.order_by('-price')
            elif get_data.get('filter', '')== 'a-z':
                objects = objects.order_by(Lower('book_title'))
            elif get_data.get('filter', '')== 'z-a':
                objects = objects.order_by('-'+Lower('book_title'))
        if get_data.get('book_title',''):
            books=models.UserBook.objects.filter(
                book_title__icontains=get_data['book_title'])
            serializer = serializers.GetUserBooksSerializer(
                books,many=True
            )
            return Response(serializer.data,status=status.HTTP_200_OK)
        elif get_data.get('all',''):
            fields = [f for f in models.UserBook._meta.fields if isinstance(f,CharField)]
            queries = [Q(**{f.name+"__icontains":get_data.get('all')}) for f in fields]
            qs = Q()
            for query in queries:
                qs = qs | query
            books = models.UserBook.objects.filter(qs)
            serializer = serializers.GetUserBooksSerializer(
                books,many=True
            )
            return Response(serializer.data,status=status.HTTP_200_OK)

        serializer = serializers.GetUserBooksSerializer(objects,many=True)
        a = Response(serializer.data,status=status.HTTP_200_OK)
        # print(a.data)
        return a

class BookStoreView(APIView):
    def get(self,request):
        objects = models.BookStore.objects.all()
        serializer = serializers.GetBookStoreSerializer(objects,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def post(self,request):
        serializer = serializers.GetUserBooksSerializer(data=request.data)
        # print(serializer)
        store = models.BookStore.objects.get(user=request.user)
        print(store)
        if serializer.is_valid():

            obj = serializer.save(store=store,created_date=datetime.datetime.now())
            msg = Notification.objects.get(title='live_start')
            send_notification(msg.content,User.objects.all(),'live',obj,msg.subtitle)

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class OneStoreView(APIView):
    def get(self,request,pk):
        objects = models.BookStore.objects.get(id=pk)
        serializer = serializers.GetBookStoreSerializer(objects)
        return Response(serializer.data,status=status.HTTP_200_OK)
