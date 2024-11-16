from django.http.response import HttpResponse
from django.shortcuts import render


def rooms(request):
    return HttpResponse('This is home page of rooms')