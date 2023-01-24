from rest_framework import serializers
from . import models


class GetBookStoreSerializer(serializers.ModelSerializer):
    user_book = serializers.SerializerMethodField()
    class Meta:
        model = models.BookStore
        fields=['pk','name','adress','phone_number','user_book']

    def get_user_book(self,obj):
        user_book = models.UserBook.objects.filter(store=obj)
        return GetUserBooksSerializer(user_book,many=True).data


class GetUserBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model =models.UserBook
        fields=['book_title','condition','language']
