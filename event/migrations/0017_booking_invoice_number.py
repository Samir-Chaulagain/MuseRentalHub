# Generated by Django 5.0.2 on 2024-02-19 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0016_alter_event_is_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='invoice_number',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
