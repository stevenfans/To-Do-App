from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'tasks/list.html')