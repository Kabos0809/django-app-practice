# Generated by Django 2.2.5 on 2021-12-23 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=' ', max_length=30)),
                ('number', models.CharField(default='2', max_length=1)),
                ('comments', models.CharField(default=' ', max_length=500)),
            ],
        ),
    ]
