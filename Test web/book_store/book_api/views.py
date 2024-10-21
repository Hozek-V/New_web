from django.shortcuts import render
from django.http import JsonResponse
from books.models import Books
from django.core import serializers
import json

def my_json_view(request):
    data = {
        "name": "Adam",
        "age": 33,
        "city": "Praha"
    }

    return JsonResponse(data)

def json_book_list(request):
    data = Books.objects.all()
    data = serializers.serialize('json', data)
    return JsonResponse(data, safe=False)


def json_book_detail(request, id):
    data = Books.objects.get(id=id)
    data = serializers.serialize('json', [data])
    return JsonResponse(data, safe=False)
