from django.db import models
from django.db.models.fields import BooleanField


# Create your models here.

class Signup(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=50, unique=True)
    type = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    last_login = models.DateTimeField()
    creation_date = models.DateTimeField()
    update_date = models.DateTimeField()


class Movie(models.Model):
    mname = models.CharField(max_length=20, unique=True)
    shortdesc = models.CharField(max_length=20, unique=True)
    longdesc = models.CharField(max_length=250, unique=True)
    review = models.CharField(max_length=250, null=True)
    vurl = models.CharField(max_length=250)
    imageurl = models.CharField(max_length=250)
    mrating = models.FloatField(max_length=20)
    creation_date = models.DateTimeField()
    update_date = models.DateTimeField()
