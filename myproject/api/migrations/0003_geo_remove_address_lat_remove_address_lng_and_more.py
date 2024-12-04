# Generated by Django 5.1.3 on 2024-12-01 16:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_user_address_alter_user_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Geo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lng', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.RemoveField(
            model_name='address',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='address',
            name='lng',
        ),
        migrations.AddField(
            model_name='address',
            name='geo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.geo'),
        ),
    ]