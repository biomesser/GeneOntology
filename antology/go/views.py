from django.http import HttpRequest, HttpResponse
from django.shortcuts import render



# Create your views here.


def about(request):
    return HttpResponse('Тренимся!')

def go_show(request):
    return HttpResponse('z')
