from api.serializers import LoginSerializer
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, serializers, status, viewsets, views
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.parsers import JSONParser


# Create your views here.
def homepage(request):
    return HttpResponse("Hello World")


class LoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        # user = User.objects.get(username=username)
        user = authenticate(request, username=username, password=password)
        login(request, user)
        if user is not None:
            return Response({
                'user': user.username
                }, status=status.HTTP_200_OK)
        else:
            return Response({
                'message': "User/password doesn't match"
            }, status=status.HTTP_400_BAD_REQUEST)


