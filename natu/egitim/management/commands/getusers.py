from django.core.management import BaseCommand
from django.core.management.base import CommandError
from egitim.models import RandomUser
from random import randint
from urllib.request import urlopen
import json


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        temp_list = []
        for i in range(1,options['count']+1):
            url= "https://randomuser.me/api/?results=%s".format(i)
            response = urlopen(url)
            data = response.read()
            data = json.loads(data)['results'][0]
            temp = RandomUser(
                name=data['name']['first'],
                lastname=data['name']['first'],
                mobile_number=data['phone'],
                age=randint(1, 100),
            )
            temp_list.append(temp)
            print("ok")
        RandomUser.objects.save_randoms(temp_list)
