from django.shortcuts import render
from django.http import HttpResponse

def index(request, template):

    return render(request, template)
