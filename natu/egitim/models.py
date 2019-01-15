from django.db import models
from django.contrib.postgres.fields import JSONField
import uuid
# Create your models here.

class Okul(models.Model):
    name_of_school = models.CharField(max_length=50)
    spening_year = models.IntegerField()
    detail = models.CharField(max_length=50, default='')

    class Meta:
        db_table = "education"


class save_random_user_manager(models.Manager):
    def generate_random_code(self):
        code = uuid.uuid4().hex

        return code

    def save_randoms(self, data):

        for i in data:
            setattr(i, 'code', self.generate_random_code())

        super(save_random_user_manager, self).bulk_create(data)


class RandomUser(models.Model):
    name = models.CharField(max_length=99)
    lastname = models.CharField(max_length=99)
    mobile_number = models.CharField(max_length=99)
    age = models.IntegerField()
    code = models.BigIntegerField()
    objects = save_random_user_manager()


class StudentDetail(models.Model):
    created_at = models.DateField()
    student_code = models.CharField(max_length=50)
    detail_data = JSONField()


class SikimsonikModel(models.Model):
    name = models.CharField(max_length=99)
    data = JSONField()
