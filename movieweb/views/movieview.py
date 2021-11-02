from datetime import datetime
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from movieweb.models import Movie, Rating
from movieweb.serialization import MovieSerializer, RatingSerializer


class AddMovie(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'movieweb/SL/signup.html')

    def post(self, request):
        data = request.POST
        movies = Movie.objects.create(mname=data['mname'],
                                        shortdesc=data['shortdesc'],
                                        longdesc=data['longdesc'],
                                        vurl=data['vurl'],
                                        imageurl=data['imageurl'],
                                        creation_date=datetime.now(),
                                        update_date=datetime.now())

        print(data['mrating'])

        Rating.objects.create(mname=movies,
                               mrating=data['mrating'],
                               noofupdate=1,
                               )
        serializer = MovieSerializer(instance=movies)
        movies = Movie.objects.values()
        return render(request, "movieweb/admin/movieslist.html", context={'alert': True, 'movies': movies})


class UpdateRating(TemplateView):
    def post(self, request):
        pick_record = Rating.objects.filter(Q(mname_id=request.POST.get("id"))).first()
        serializer = RatingSerializer(pick_record)
        prerate=int(serializer.data['mrating'])
        noofrating = int(serializer.data['noofupdate'])+1
        newrate=int(request.POST.get("rating"))
        total=prerate+newrate/noofrating
        round(total)
        serializer = RatingSerializer(pick_record,
                                      data={'mrating':total,'noofupdate':noofrating }, partial=True)
        if serializer.is_valid():
            serializer.save()
        return redirect("userview")


class EditMovie(TemplateView):
    def get(self, request, **kwargs):
        # users = Movie.objects.get()
        # serializer = MovieSerializer(users)
        # # print(serializer.data)
        movies = Movie.objects.values()
        ratings = Rating.objects.values()
        print(ratings)
        for m in movies:
            for r in ratings:
                if r['mname_id'] == m['id']:
                    m['rating']=r['mrating']
        return render(request, 'movieweb/admin/movieslist.html', {'movies': movies})

    def post(self, request):
        Movie.objects.filter(Q(mname=request.POST.get('custId', ))).delete()
        user = Movie.objects.values()
        return render(request, 'movieweb/admin/movieslist.html', {'movies': user})


class UpdateMovie(TemplateView):
    def post(self, request):
        data = request.POST
        pick_record = Movie.objects.filter(Q(mname=data['mname'])).first()
        movies = Movie.objects.values()

        serializer = MovieSerializer(pick_record, data={'mname': data['mname'],
                                                        'shortdesc': data['shortdesc'],
                                                        'longdesc': data['longdesc'],
                                                        'vurl': data['vurl'],
                                                        'imageurl': data['imageurl'],
                                                        'update_date': datetime.now()}, partial=True)
        if serializer.is_valid():
            serializer.save()
        return render(request, "movieweb/admin/movieslist.html", context={'alert': True, 'movies': movies})
