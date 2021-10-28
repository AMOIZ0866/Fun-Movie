from rest_framework import serializers

from movieweb.models import Signup, Movie


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
