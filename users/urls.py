from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/',views.OneUserView.as_view(),name = 'oneuser'),
    path('',views.UserView.as_view(),name = 'user'),
    path('registration/',views.RegisterView.as_view(),name='register')

]
