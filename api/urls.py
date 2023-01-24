from django.urls import path
from . import views

urlpatterns = [
    path('book-store/',views.BookStoreView.as_view(),name='bookstore'),
    path('user-book/',views.UserBookView.as_view(),name='userbook'),
    path('book-store/<int:pk>',views.OneStoreView.as_view(),name='onebookstore')
    # path('all-store/',views.AllBookStoreView.as_view(),name='allbookstore'),
    # path('aaa/',views.GetStoreWithBookView.as_view(),name='getstorewithbookview'),

]
