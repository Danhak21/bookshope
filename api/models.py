from django.db import models
from users.models import User as USER
# Create your models here.

class BookStore(models.Model):
    name = models.CharField(max_length=50)
    adress=models.CharField(max_length=50)
    phone_number=models.IntegerField()
    store_image=models.ImageField(upload_to=None,null=True,blank=True)
    user = models.ForeignKey(USER,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name

class UserBook(models.Model):
    store = models.ForeignKey(BookStore,on_delete = models.CASCADE, related_name='books' )
    book_title = models.CharField(max_length=250)
    condition = models.CharField(max_length=50)
    language = models.CharField(max_length = 250)
    author = models.CharField(max_length=250)
    book_publisher=models.CharField(max_length=250)
    publish_year=models.DateField(null=True,blank=True)
    created_date=models.DateTimeField()
    book_thumbnai=models.ImageField(upload_to=None,null=True,blank=True)
    description=models.TextField()

    def __str__(self):
            return self.book_title
