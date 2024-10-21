from django.shortcuts import render
from django.http import JsonResponse, FileResponse
from books.models import Books
from django.core import serializers
import json
from django.conf import settings
import os

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


def my_file(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'files', 'ukol.txt')

    #return FileRespose(open(file_path, 'rb'), filename='download.txt') #zobrazení
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='download.txt')

def my_img(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'img', 'anchor.png')

    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='download.png')
