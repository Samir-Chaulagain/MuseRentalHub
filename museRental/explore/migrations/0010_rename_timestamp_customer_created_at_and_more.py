# Generated by Django 4.2.6 on 2023-11-21 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0009_alter_item_item_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='saved_item',
            old_name='timestamp',
            new_name='created_at',
        ),
    ]
