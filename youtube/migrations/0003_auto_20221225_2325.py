# Generated by Django 3.2.14 on 2022-12-25 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0002_apikeys'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='APIKeys',
            new_name='APIKey',
        ),
        migrations.AlterModelTable(
            name='apikey',
            table='api_keys',
        ),
    ]
