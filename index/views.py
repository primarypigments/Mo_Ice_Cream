from django.shortcuts import render
from django.http import HttpResponse

def my_index(request):
    return HttpResponse("Hello, Index!")