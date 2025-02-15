# Generated by Django 5.0.4 on 2024-06-01 01:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0010_alter_imagetrack_datetimetrack_alter_imagetrack_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='error_form',
            name='date_log_error',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 31, 20, 46, 45, 393071, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='error_form',
            name='image_error',
            field=models.FileField(max_length=500, upload_to='screen/static/ErrorFormImg'),
        ),
        migrations.AlterField(
            model_name='imagetrack',
            name='DateTimeTrack',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 31, 20, 46, 45, 392071, tzinfo=datetime.timezone.utc)),
        ),
    ]
