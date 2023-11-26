from rest_framework import serializers
from .models import Farmers, FarmDetails, Amkosi, Crops

class FarmersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmers
        fields = ('farmer_name', 'bank_name', 'type_of_crops', 'quant_of_products', 'total_cost_production', 'email', 'phone_no', 'location')

class FarmDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmDetails
        fields = ('owner_of_farm', 'size_of_farm', 'no_of_farms', 'assets_available', 'physical_location')

class CropsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crops
        fields = ('crop_name', 'crop_owner', 'quant_of_crops')

class AmkosiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amkosi
        fields = ('assoc_name', 'assoc_email', 'location', 'assoc_phone_no')
