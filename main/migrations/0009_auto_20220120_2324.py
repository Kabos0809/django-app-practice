# Generated by Django 3.2.4 on 2022-01-20 14:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20220120_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangeinfomodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 20, 14, 24, 44, 482086, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 20, 14, 24, 44, 482086, tzinfo=utc)),
        ),
    ]
