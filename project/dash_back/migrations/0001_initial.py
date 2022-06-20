# Generated by Django 2.2.26 on 2022-06-20 21:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flexi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flexiDev', models.CharField(max_length=300)),
                ('response_time', models.DateTimeField(default=datetime.datetime(2022, 6, 21, 0, 16, 3, 589380))),
                ('res_pow', models.FloatField()),
                ('res_durr', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Online',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev', models.CharField(max_length=300)),
                ('saved_date', models.DateTimeField(default=datetime.datetime(2022, 6, 21, 0, 16, 3, 586380))),
                ('pow', models.FloatField()),
                ('ready', models.IntegerField(default=0, null=True)),
                ('signal', models.IntegerField(default=0, null=True)),
                ('providing', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devId', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2022, 6, 21, 0, 16, 3, 581380))),
                ('value', models.FloatField()),
                ('grid', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2022, 6, 21, 0, 16, 3, 588382))),
                ('value', models.FloatField()),
            ],
        ),
    ]
