# Generated by Django 3.2.4 on 2022-03-01 02:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20220301_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='threadcomments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 1, 2, 43, 10, 866051)),
        ),
        migrations.AlterField(
            model_name='threadmodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 1, 2, 43, 10, 866051)),
        ),
    ]