from django.db.models import fields
from rest_framework import serializers
from .models import *

class CropDiseaseAPISerializers(serializers.ModelSerializer):
    class Meta:
        model = CropDiseaseAPI
        fields = '__all__'

class FarmerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Farmers
        fields = '__all__'
