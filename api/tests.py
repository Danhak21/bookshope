from django.test import TestCase
from django.urls import reverse, resolve
from api import views, serializers, models
from django.test import TestCase
from users.models import User


from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token
from json import JSONEncoder

from collections import OrderedDict




class TestUrls(TestCase):
    def test_user_book_url_is_resolves(self):
        url = reverse('userbook')
        self.assertEquals(resolve(url).func.view_class, views.UserBookView)

    def test_book_store_url_is_resolves(self):
        url = reverse('bookstore')
        self.assertEquals(resolve(url).func.view_class, views.BookStoreView)

    def test_one_book_store_url_is_resolves(self):
        url = reverse('onebookstore', args=[1])
        self.assertEquals(resolve(url).func.view_class, views.OneStoreView)


class BookStoreViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            id=1, email='test@host.com', password='bestpass')



        self.client1 = APIClient()
        self.client1.login(email='test@host.com', password='123456')

        self.user_token = Token.objects.create(user=self.user)

        self.store = models.BookStore.objects.create(
            name = "Test1",
            adress = "Testavan1",
            phone_number = "0546965871",
            user = self.user
        )
        self.store2 = models.BookStore.objects.create(
            name = "Test1",
            adress = "Testavan1",
            phone_number = "0546965871",

        )
        self.book = models.UserBook.objects.create(
            store=self.store2,
            book_title='gago',
            condition = 'faffa',
            language = 'hay',
            author = 'mmmm',
            book_publisher= 'oppppp',
            publish_year = '2022-12-23',
            created_date = '2022-12-23T00:00:00Z',
            book_thumbnai = '',
            description = 'hhhhh'
        )
        self.book2 = models.UserBook.objects.create(
            store=self.store2,
            book_title='gago1',
            condition = 'faffa1',
            language = 'hay1',
            author = 'mmmm1',
            book_publisher= 'oppppp',
            publish_year = '2022-12-23',
            created_date = '2022-12-23T00:00:00Z',
            book_thumbnai = '',
            description = 'hhhhh1'
        )

    def test_bookStores_list_view(self):
        response = self.client.get(reverse("bookstore"))
        response_date = response.data
        # print(response_date)
        serializer_data = [
            OrderedDict(serializers.GetBookStoreSerializer(self.store).data),
            OrderedDict(serializers.GetBookStoreSerializer(self.store2).data)
        ]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_date, serializer_data)

    def test_bookStores_list_post_view(self):

        self.client.credentials(HTTP_AUTHORIZATION="Token "+self.user_token.key)

        data ={

                'book_title':'fkyukl',
                'condition':'cyyjj',
                'language':'hay',
        }
        # print(data)
        request = self.client.post(reverse("bookstore"),data,format='json')
        # print(request)
        self.assertEqual(request.status_code,201)


    def test_bookStores_list_books_view(self):
        response = self.client.get(reverse("userbook"))
        response_date = response.data
        # print(response_date)
        serializer_data = [
            OrderedDict(serializers.GetUserBooksSerializer(self.book).data),
            OrderedDict(serializers.GetUserBooksSerializer(self.book2).data)
        ]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_date, serializer_data)


    # def test_bookStores_list_one_view(self):
    #     response = self.client.get(reverse('onebookstore', args=[1]))
    #     response_date = response.data
    #     print(response_date)
