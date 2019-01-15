from rest_framework import serializers
from egitim.models import Okul, SikimsonikModel

class SSerializer(serializers.ModelSerializer):
    class Meta:
        model = Okul
        fields = ('name_of_school',)

class AddSchoolSerializer(serializers.ModelSerializer):
    name_of_school_ = serializers.CharField()
    name_of_school_ = serializers.IntegerField()
    name_of_school_ = serializers.CharField()

class SikimsonikSerializer(serializers.ModelSerializer):
    class Meta:
        model = SikimsonikModel
        fields = ('name', 'code')
