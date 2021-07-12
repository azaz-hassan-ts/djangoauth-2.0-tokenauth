from django.contrib.auth import models
from django.contrib.auth.models import User
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from rest_framework.fields import CharField
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    class Meta:
        model = User
        fields = ('username', 'password')