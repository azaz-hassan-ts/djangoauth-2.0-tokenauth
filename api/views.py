from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, serializers, status, viewsets, views
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import authentication_classes, permission_classes
from .serializers import RegistrationSerializer, LoginSerializer
from rest_framework.authentication import BasicAuthentication


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
            login(request, user)
            return Response(
                {"user": username, "password": password}, status=status.HTTP_200_OK
            )
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
