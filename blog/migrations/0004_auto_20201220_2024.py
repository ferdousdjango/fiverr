# Generated by Django 3.0.5 on 2020-12-20 14:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201220_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 12, 20, 14, 24, 12, 77821, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, max_length=600, upload_to='blog/images/'),
        ),
    ]
