# Generated by Django 4.1.5 on 2023-02-03 09:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_trip_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 4, 9, 17, 39, 2850)),
        ),
    ]
