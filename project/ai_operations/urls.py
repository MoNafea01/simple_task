
from django.urls import path
#from .views import train_test_split_view
from . import views



urlpatterns = [
    #path('train-test-split/', train_test_split_view, name='train_test_split'),
    path('', views.home, name="home"),
    path('room1/', views.room1, name="room1"),
    path('execute/', views.execute_function, name= 'execute_function'),
    
]