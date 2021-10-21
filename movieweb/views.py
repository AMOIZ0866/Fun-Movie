from django.shortcuts import render



# Create your views here.
from django.template import context


def home(request):
    return render(request, 'movieweb/base.html')
