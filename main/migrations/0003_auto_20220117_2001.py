# Generated by Django 3.2.4 on 2022-01-17 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_reportmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportmodel',
            old_name='title',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='reportmodel',
            name='article_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
