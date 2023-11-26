from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FarmersSerializer, FarmDetailsSerializer, AmkosiSerializer, CropsSerializer
from .models import Farmers, FarmDetails, Crops, Amkosi

class FarmersView(viewsets.ModelViewSet):
    serializer_class = FarmersSerializer
    queryset = Farmers.objects.all()

class FarmDetailsView(viewsets.ModelViewSet):
    serializer_class = FarmDetailsSerializer
    queryset = FarmDetails.objects.all()

class CropsView(viewsets.ModelViewSet):
    serializer_class = CropsSerializer
    queryset = Crops.objects.all()

class AmkosiView(viewsets.ModelViewSet):
    serializer_class = AmkosiSerializer
    queryset = Amkosi.objects.all()