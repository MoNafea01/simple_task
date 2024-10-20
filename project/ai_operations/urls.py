
from django.urls import path
from .views import train_test_split_view


urlpatterns = [
    path('train-test-split/', train_test_split_view, name='train_test_split'),
]