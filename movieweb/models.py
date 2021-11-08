from django.db import models


class Movie(models.Model):
    mname = models.CharField(max_length=20, unique=True)
    shortdesc = models.CharField(max_length=20, unique=True)
    longdesc = models.CharField(max_length=250, unique=True)
    review = models.CharField(max_length=250, null=True)
    vurl = models.CharField(max_length=250)
    imageurl = models.CharField(max_length=250)
    creation_date = models.DateTimeField()
    update_date = models.DateTimeField()


class Rating(models.Model):
    mname = models.ForeignKey(Movie, related_name='rating', on_delete=models.CASCADE)
    mrating = models.FloatField()
    noofupdate = models.IntegerField()
