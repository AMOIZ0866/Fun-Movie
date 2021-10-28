from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from movieweb.models import Signup


class UserLogin(TemplateView):
    def get(self, request):
        return render(request, 'movieweb/SL/login.html')

    def post(self, request):
        data = request.POST
        if Signup.objects.filter(Q(username=data['username']) & Q(password=data['password']) & Q(type=True)):
            return redirect('adminview')
        elif Signup.objects.filter(Q(username=data['username']) & Q(password=data['password']) & Q(type=False)):
            return redirect('userview')
        else:
            return redirect('login')


