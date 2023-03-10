# Generated by Django 4.1.5 on 2023-01-28 20:45

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='phoneNum',
            field=phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128, region=None, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='course_bought',
            field=models.ManyToManyField(to='users.course'),
        ),
    ]
