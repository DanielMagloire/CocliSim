# Generated by Django 3.2 on 2021-04-22 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coclisim', '0002_calcclass'),
    ]

    operations = [
        migrations.AddField(
            model_name='calcclass',
            name='result',
            field=models.IntegerField(default=0),
        ),
    ]
