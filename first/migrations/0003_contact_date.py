# Generated by Django 3.1.7 on 2021-03-01 08:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 3, 1, 8, 11, 45, 325716, tzinfo=utc)),
        ),
    ]
