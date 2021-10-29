from django.db.models import Q
from django.shortcuts import render, redirect
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



class ViewUserProfile(TemplateView):
    def post(self, request):
        data = request.POST.get('username')
        userdetails = Signup.objects.filter(Q(username=data)).values().first()
        print(userdetails)
        return render(request, 'movieweb/user/uprofile.html', context={'userdetails': userdetails})


class UpdateUserProfile(TemplateView):
    def post(self, request):
        data = request.POST
        movies = Movie.objects.values()
        userdetails = Signup.objects.filter(Q(username=data['username'])).first()
        serializer = CreateUserSerializer(userdetails,data={
            'password': data['password'],
            'email': data['email'],
            'update_date': datetime.now()}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return render(request,'movieweb/user/uprofile.html', context={'alert':True, 'user':data['username'],'userdetails':userdetails})
        else:
            emessage = serializer.errors
            print(emessage)
            if str(emessage.keys()) == "odict_keys(['email'])":
                error = "This Email is Already Registered"
            elif str(emessage.keys()) == "odict_keys(['username'])":
                error = "This Username is Already Registered"
            elif str(emessage.keys()) == "odict_keys(['username', 'email'])":
                error = "This Username And Email is Already Registered"
            else:
                error = "Password Error"
            return render(request, 'movieweb/user/uprofile.html', context={'error': True, 'text': error,'user':data['username'],'userdetails':userdetails})

