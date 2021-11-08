from django.contrib import admin

from movieweb.models import  Movie, Rating

# Register your models here.
admin.site.register(Movie)
admin.site.register(Rating)
