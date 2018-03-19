# Generated by Django 2.0.2 on 2018-03-19 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kindergarten_app', '0006_auto_20180319_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='second_name',
        ),
        migrations.AlterField(
            model_name='child',
            name='group',
            field=models.IntegerField(choices=[(0, 'UNDEFINED'), (2, 'BLUE GROUP'), (1, 'GREEN GROUP')], default=0),
        ),
    ]