# Generated by Django 2.2.5 on 2021-12-29 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211230_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='Youtube_url',
            field=models.CharField(blank=True, max_length=100, verbose_name='YouTube CHANNEL'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='twitter_id',
            field=models.CharField(blank=True, max_length=100, verbose_name='twitter id'),
        ),
    ]