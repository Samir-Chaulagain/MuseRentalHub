# Generated by Django 5.0.2 on 2024-02-11 20:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='time',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
    ]
