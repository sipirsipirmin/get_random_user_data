from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from egitim.serializers import SSerializer
from egitim.models import RandomUser
# Create your views here.


class RandomUserView(APIView):
    def get(self, request, format=None):
        users = RandomUser.objects.all()
        serializer = SSerializer(users, many=True)

        return Response(serializer.data)

    
