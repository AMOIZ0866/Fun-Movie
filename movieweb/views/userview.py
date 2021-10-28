from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime
from movieweb.models import Movie, Signup
from movieweb.serialization import MovieSerializer, CreateUserSerializer


class Userview(TemplateView):
    def get(self, request, **kwargs):
        movies = Movie.objects.values()
        return render(request, 'movieweb/user/userhome.html', {'movies': movies})

    def post(self, request):
        data = request.POST
        movies = Movie.objects.filter(Q(mname=data['name']))
        print(movies)
        return render(request, 'movieweb/user/userhome.html', {'movies': movies})



