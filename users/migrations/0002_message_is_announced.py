# Generated by Django 4.1.5 on 2023-01-26 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_announced',
            field=models.BooleanField(default=False),
        ),
    ]