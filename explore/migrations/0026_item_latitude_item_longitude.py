# Generated by Django 4.2.7 on 2024-02-06 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0025_customer_latitude_customer_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]