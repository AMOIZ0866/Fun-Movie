from datetime import datetime
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from movieweb.models import Movie
from movieweb.serialization import MovieSerializer


class AddMovie(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'movieweb/SL/signup.html')

    def post(self, request):
        data = request.POST
        serializer = MovieSerializer(data={'mname': data['mname'],
                                           'shortdesc': data['shortdesc'],
                                           'longdesc': data['longdesc'],
                                           'vurl': data['vurl'],
                                           'imageurl': data['imageurl'],
                                           'mrating': data['mrating'],
                                           'creation_date': datetime.now(),
                                           'update_date': datetime.now()})
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return redirect('editmovie')


class UpdateRating(TemplateView):
    def post(self, request):
        pick_record = Movie.objects.filter(Q(mname=request.POST.get("id", ))).first()
        serializer = MovieSerializer(pick_record,
                                     data={'mrating': request.POST.get("rating", ), 'review': request.POST.get(
                                         "review", )}, partial=True)
        if serializer.is_valid():
            serializer.save()
        return redirect("userview")


class EditMovie(TemplateView):
    def get(self, request, **kwargs):
        user = Movie.objects.values()
        return render(request, 'movieweb/admin/movieslist.html', {'movies': user})

    def post(self, request):
        Movie.objects.filter(Q(mname=request.POST.get("id", ))).delete()
        user = Movie.objects.values()
        return render(request, 'movieweb/admin/movieslist.html', {'movies': user})


class UpdateMovie(TemplateView):
    def post(self, request):
        data = request.POST
        pick_record = Movie.objects.filter(Q(mname=data['mname'])).first()

        serializer = MovieSerializer(pick_record, data={'mname': data['mname'],
                                                        'shortdesc': data['shortdesc'],
                                                        'longdesc': data['longdesc'],
                                                        'vurl': data['vurl'],
                                                        'imageurl': data['imageurl'],
                                                        'mrating': data['mrating'],
                                                        'update_date': datetime.now()}, partial=True)
        if serializer.is_valid():
            serializer.save()
        return redirect("editmovie")
