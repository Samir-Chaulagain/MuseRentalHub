# Generated by Django 4.2.7 on 2023-11-25 12:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0012_remove_item_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='instrument_image1',
            field=models.ImageField(default='img/inst1/', upload_to='img/instrument_images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]),
        ),
        migrations.AlterField(
            model_name='item',
            name='instrument_image2',
            field=models.ImageField(default='img/inst1/', upload_to='img/instrument_images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]),
        ),
        migrations.AlterField(
            model_name='item',
            name='instrument_image3',
            field=models.ImageField(default='img/inst1/', upload_to='img/instrument_images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]),
        ),
    ]
