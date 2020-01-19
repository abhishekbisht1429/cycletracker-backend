from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Cycle
from .serializers import UserSerializer, CycleSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CycleViewSet(viewsets.ModelViewSet):
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer
    