from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from movieweb.models import  Movie


class HomeUser(TemplateView):
    def get(self,request):
        return render(request,'movieweb/home.html')