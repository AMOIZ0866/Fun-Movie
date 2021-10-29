from datetime import datetime
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from sweetify import sweetify

from movieweb.serialization import CreateUserSerializer


class UserSignUp(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'movieweb/SL/signup.html')

    def post(self, request):
        data = request.POST
        serializer = CreateUserSerializer(data={'username': data['username'],
                                                'password': data['password'],
                                                'email': data['email'],
                                                'last_login': datetime.now(),
                                                'creation_date': datetime.now(),
                                                'update_date': datetime.now()})
        if serializer.is_valid():
            serializer.save()
            return redirect('/movies/login')
        else:
            emessage = serializer.errors
            error=""
            if str(emessage.keys()) == "odict_keys(['email'])":
                error="This Email is Already Registered"
            elif str(emessage.keys()) == "odict_keys(['username'])":
                error = "This Username is Already Registered"
            else:
                error = "Password Error"
            return render(request, 'movieweb/SL/signup.html', context={'error':True, 'text':error})
