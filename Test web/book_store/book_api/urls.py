from django.urls import path
from .views import *

urlpatterns = [
    path('', json_book_list, name='json_book_list'),
    path('<int:id>/', json_book_detail, name='json_book_detail'),
    path('test/', my_json_view, name='test'),
    path('file/', my_file, name='file'),
    path('img/', my_img, name='img'),
]