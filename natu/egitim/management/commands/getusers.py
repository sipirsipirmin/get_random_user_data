import logging
from flask import jsonify
from django.core.management import BaseCommand
from django.core.management.base import CommandError
from egitim.models import Okul, RandomUser
from urllib.request import urlopen
import json

logger = logging.getLogger('main')

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        CommandError("OK!")
        temp_list = []
        for i in range(1,5):
            url= "https://randomuser.me/api/?results=%s".format(i)
            response = urlopen(url)
            data = response.read()
            data = json.loads(data)
            temp = RandomUser(
                name=data['results'][0]['name']['first'],
                lastname=data['results'][0]['name']['first'],
                mobile_number=data['results'][0]['phone'],
                age=5,
            )
            temp_list.append(temp)
            print("ok")
        RandomUser.objects.save_randoms(temp_list)
