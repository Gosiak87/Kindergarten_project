# Generated by Django 2.0.2 on 2018-03-20 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kindergarten_app', '0013_auto_20180320_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='group',
            field=models.IntegerField(choices=[(0, 'Nieokreślona'), (2, 'Grupa Niebieska'), (1, 'Grupa Zielona')], default=0),
        ),
    ]
