# Generated by Django 2.0.2 on 2018-03-19 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kindergarten_app', '0010_auto_20180319_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='year_of_birth',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='group',
            field=models.IntegerField(choices=[(2, 'Grupa Niebieska'), (1, 'Grupa Zielona'), (0, 'Nieokreślona')], default=0),
        ),
    ]