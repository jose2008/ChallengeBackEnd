# Generated by Django 2.1.2 on 2019-05-30 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=60),
        ),
    ]
