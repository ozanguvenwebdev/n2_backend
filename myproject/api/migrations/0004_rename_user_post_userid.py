# Generated by Django 5.1.3 on 2024-12-01 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_geo_remove_address_lat_remove_address_lng_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='userId',
        ),
    ]