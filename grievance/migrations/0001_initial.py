# Generated by Django 2.2.1 on 2019-09-15 08:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='problems',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2019, 9, 15, 14, 14, 52, 301244))),
                ('ptype', models.CharField(max_length=20)),
                ('reporter', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('department', models.CharField(max_length=50)),
            ],
        ),
    ]
