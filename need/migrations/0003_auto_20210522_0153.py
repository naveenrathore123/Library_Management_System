# Generated by Django 3.1.7 on 2021-05-21 20:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('need', '0002_auto_20210522_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrecord',
            name='DueDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 6, 1, 53, 7, 461688)),
        ),
        migrations.AlterField(
            model_name='historyrecord',
            name='ReturnDate',
            field=models.DateTimeField(),
        ),
    ]