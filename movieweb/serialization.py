from rest_framework import serializers
from rest_framework.authtoken.admin import User

from movieweb.models import Signup, Movie, Rating


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password','is_staff']

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['mname', 'shortdesc', 'longdesc', 'review', 'vurl', 'imageurl', 'creation_date',
                  'update_date', 'rating']

        def create(self, validated_data):
            ratings_data = validated_data.pop('mrating')
            mname = Rating.objects.create(**validated_data)
            for ratings_data in ratings_data:
                Rating.objects.create(mname=mname, **ratings_data)
            return mname


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
