# Generated by Django 5.0.6 on 2024-07-01 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='healthcarefacility',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='healthcarefacility',
            name='longitude',
        ),
    ]
