# Generated by Django 2.0.2 on 2018-03-19 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kindergarten_app', '0009_auto_20180319_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='group',
            field=models.IntegerField(choices=[(2, 'Grupa Niebieska'), (0, 'Nieokreślona'), (1, 'Grupa Zielona')], default=0),
        ),
    ]
