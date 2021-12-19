from django.http import HttpResponse
from django.shortcuts import render

from . import templates

def index(request):
    context = {}

    return render(request, 'mysite/index.html', context)

