from datetime import datetime
from django.shortcuts import render
from django.views.generic import TemplateView
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
        else:
            print(serializer.errors)
        return render(request, 'movieweb/SL/signup.html')



