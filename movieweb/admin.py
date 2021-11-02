from django.contrib import admin

from movieweb.models import Signup, Movie, Rating

# Register your models here.
admin.site.register(Signup)
admin.site.register(Movie)
admin.site.register(Rating)
