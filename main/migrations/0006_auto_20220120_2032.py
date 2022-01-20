# Generated by Django 3.2.4 on 2022-01-20 11:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20220120_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangeinfomodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 20, 11, 32, 29, 321791, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('created', models.DateTimeField(default=datetime.datetime(2022, 1, 20, 11, 32, 29, 321791, tzinfo=utc))),
                ('update', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='exchangeinfomodel',
            name='thread',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='main.thread'),
        ),
        migrations.DeleteModel(
            name='ExchangeInfoThread',
        ),
    ]
