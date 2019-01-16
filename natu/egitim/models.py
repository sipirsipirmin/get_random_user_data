from django.db import models
from django.contrib.postgres.fields import JSONField
import uuid
# Create your models here.


class save_random_user_manager(models.Manager):
    def generate_random_code(self):
        code = uuid.uuid4().int % 10**8
        if super(save_random_user_manager, self).filter(code=code).first():
            self.generate_random_code()
        return code

    def save_randoms(self, data):
        for i in data:
            setattr(i, 'code', self.generate_random_code())
        super(save_random_user_manager, self).bulk_create(data)

    def save_post(self, data):
        data['code'] = self.generate_random_code()
        super(save_random_user_manager, self).create(**data)


class RandomUser(models.Model):
    name = models.CharField(max_length=99)
    lastname = models.CharField(max_length=99)
    mobile_number = models.CharField(max_length=99)
    age = models.IntegerField()
    code = models.BigIntegerField()
    objects = save_random_user_manager()
