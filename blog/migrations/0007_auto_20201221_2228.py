# Generated by Django 3.0.5 on 2020-12-21 16:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20201221_2214'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Quote',
        ),
        migrations.AddField(
            model_name='blog',
            name='quote',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 12, 21, 16, 28, 32, 926173, tzinfo=utc)),
        ),
    ]
