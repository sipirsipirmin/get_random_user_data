from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.views import APIView
from egitim.serializers import SSerializer, SikimsonikSerializer
from egitim.models import Okul, SikimsonikModel
# Create your views here.


class OkulView(APIView):
    def get(self, request, format=None):
        okul = Okul.objects.all()
        serializer = SSerializer(okul, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        pass

class SikimsonikView(APIView):
    def get(self, request, farmat=None):
        sikimsoniks = SikimsonikModel.objects.all()
        serializer = SikimsonikSerializer(sikimsoniks, many=True)

        return Response(serializer.data)
