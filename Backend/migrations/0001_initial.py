# Generated by Django 4.1.1 on 2022-10-16 09:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('projectID', models.AutoField(primary_key=True, serialize=False)),
                ('creatorId', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=500)),
                ('category', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=10000)),
                ('image', models.CharField(max_length=1000)),
                ('minPrice', models.IntegerField()),
                ('targetPrice', models.IntegerField()),
                ('isFeatured', models.BooleanField(default=False)),
                ('total', models.IntegerField(default=0)),
                ('donateCount', models.IntegerField(default=0)),
                ('createAt', models.DateTimeField(default=datetime.datetime(2022, 10, 16, 16, 1, 34, 989896))),
            ],
        ),
    ]