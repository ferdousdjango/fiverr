# Generated by Django 3.0.5 on 2020-12-20 14:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='blog/images/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 12, 20, 14, 1, 52, 554147, tzinfo=utc)),
        ),
    ]
