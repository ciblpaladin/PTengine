# Generated by Django 5.0.4 on 2024-05-08 22:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0004_imagetrack_datetimetrack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagetrack',
            name='DateTimeTrack',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 8, 22, 9, 46, 733700, tzinfo=datetime.timezone.utc)),
        ),
    ]
