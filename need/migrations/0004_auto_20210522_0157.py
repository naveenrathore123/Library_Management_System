# Generated by Django 3.1.7 on 2021-05-21 20:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('need', '0003_auto_20210522_0153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historyrecord',
            name='ReturnDate',
        ),
        migrations.AlterField(
            model_name='bookrecord',
            name='DueDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 6, 1, 57, 16, 62171)),
        ),
    ]