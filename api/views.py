import re
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, serializers, status, viewsets, views
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import authentication_classes, permission_classes
from .serializers import RegistrationSerializer, LoginSerializer, LogoutSerializer
from rest_framework.authentication import BasicAuthentication
import requests
from django.contrib import auth

# Create your views here.
def homepage(request):
    return HttpResponse("Hello World")


class LoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    parser_classes = [JSONParser]

    def post(self, request):
        if request.data == {}:
            return Response(
                {"message": "Send request Body"}, status=status.HTTP_204_NO_CONTENT
            )

        username = request.data["username"]
        password = request.data["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            url = "http://localhost:8000/api-token-auth/"
            data = {"username": username, "password": password}
            token = requests.post(url, data=data)
            login(request, user)
            token = token.text.split('\\')
            return Response({
                "token": token[0][10:-2]
                }, status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": "User/password doesn't match"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request, format=None):
        if request.data == {}:
            return Response(
                {"message": "Send request Body"}, status=status.HTTP_204_NO_CONTENT
            )

        register_serializer = RegistrationSerializer(data=request.data)
        if register_serializer.is_valid():
            register_serializer.save()
            return Response(
                {
                    "data": register_serializer.data,
                    "message": "You are succesfully registered",
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(register_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(generics.CreateAPIView):
    authentication_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)