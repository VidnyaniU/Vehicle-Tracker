from django.shortcuts import render
from rest_framework import viewsets
from .models import Vehicle, Journey
from .serializers import VehicleSerializer, JourneySerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class JourneyViewSet(viewsets.ModelViewSet):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer

