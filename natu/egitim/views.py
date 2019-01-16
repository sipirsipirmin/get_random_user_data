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

    def post(self, request, format=None):
        serializer = SSerializer(data=request.data)
        #import ipdb; ipdb.set_trace()
        if serializer.is_valid():
            print("data is valid BİÇ")
            RandomUser.objects.save_post(serializer.data)

            return Response("Ok!", status=status.HTTP_201_CREATED)
        return Response("", status=status.HTTP_400_BAD_REQUEST)
