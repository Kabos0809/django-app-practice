# Generated by Django 3.2.10 on 2022-01-08 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_article_form_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='last_name',
        ),
    ]