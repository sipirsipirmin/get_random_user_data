# Generated by Django 2.1.5 on 2019-01-15 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egitim', '0006_auto_20190115_0706'),
    ]

    operations = [
        migrations.CreateModel(
            name='RandomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=99)),
                ('lastname', models.CharField(max_length=99)),
                ('mobile_number', models.CharField(max_length=99)),
                ('age', models.IntegerField()),
                ('code', models.BigIntegerField()),
            ],
        ),
    ]
