# Generated by Django 2.0.2 on 2018-03-18 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kindergarten_app', '0002_trip_trip_guardian'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='date',
            field=models.DateField(),
            preserve_default=False,
        ),
    ]
