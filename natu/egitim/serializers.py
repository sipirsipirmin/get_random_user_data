from rest_framework import serializers
from egitim.models import RandomUser

class SSerializer(serializers.ModelSerializer):
    class Meta:
        model = RandomUser
        fields = ('name', 'lastname', 'mobile_number', 'age')
