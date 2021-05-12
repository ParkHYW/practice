# Generated by Django 3.2 on 2021-05-08 07:45

from django.db import migrations, models
from django.db.models import fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('writer', models.CharField(max_length=100)),
                ('pub_date', models.DateField()),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name',models.CharField(max_length=50)),
                ('age',models.CharField(max_length=50)),
                ('MBTI',models.CharField(max_length=50)),
                ('Food',models.CharField(max_length=50)),
                ('hobby',models.CharField(max_length=50)),
            ],
        ),
    ]
