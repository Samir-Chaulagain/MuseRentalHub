# Generated by Django 4.2.7 on 2023-11-25 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0013_alter_item_instrument_image1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='instrument_image1',
            field=models.ImageField(default='img/inst1/', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='instrument_image2',
            field=models.ImageField(default='img/inst1/', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='instrument_image3',
            field=models.ImageField(default='img/inst1/', upload_to='images/'),
        ),
    ]
