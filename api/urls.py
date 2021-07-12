from django.conf.urls import url
from django.urls.conf import path
from . import views

urlpatterns = [
   path('login/', views.LoginView.as_view(), name="login")
]