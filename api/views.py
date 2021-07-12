from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import generics, serializers, status, viewsets, views
from django.contrib.auth.models import User
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegistrationSerializer
from rest_framework.authentication import BasicAuthentication


# Create your views here.
def homepage(request):
    return HttpResponse("Hello World")


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes=(AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request, format=None):
        if request.data == {}:
            return Response({
                'message': "Send request Body"
            }, status=status.HTTP_204_NO_CONTENT) 

        register_serializer = RegistrationSerializer(data=request.data)
        if register_serializer.is_valid():
            register_serializer.save()
            return Response(
                {
                    'data': register_serializer.data,
                    'message': "You are succesfully registered" 
                },
                status=status.HTTP_201_CREATED
            )
        return Response(register_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
