# Generated by Django 3.2.4 on 2022-01-21 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20220121_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='user',
        ),
        migrations.DeleteModel(
            name='ExchangeInfoModel',
        ),
        migrations.DeleteModel(
            name='Thread',
        ),
    ]
