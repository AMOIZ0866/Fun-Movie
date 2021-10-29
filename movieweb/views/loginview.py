from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from movieweb.models import Signup, Movie


class UserLogin(TemplateView):
    def get(self, request):
        return render(request, 'movieweb/SL/login.html')

    def post(self, request):
        data = request.POST
        movies = Movie.objects.values()
        if Signup.objects.filter(Q(username=data['username']) & Q(password=data['password']) & Q(type=True)):
            return render(request,'movieweb/admin/adminhome.html',context={'user':data['username'],'movies':movies})
        elif Signup.objects.filter(Q(username=data['username']) & Q(password=data['password']) & Q(type=False)):
            return render(request,'movieweb/user/userhome.html',context={'user':data['username'],'movies':movies})
        else:
            return render(request, 'movieweb/SL/login.html', context={'error': True, 'text': "Invalid Username Or Password"})


