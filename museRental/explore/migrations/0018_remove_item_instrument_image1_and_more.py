# Generated by Django 4.2.7 on 2024-01-21 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0017_item_is_sellable_alter_item_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='instrument_image1',
        ),
        migrations.RemoveField(
            model_name='item',
            name='instrument_image2',
        ),
        migrations.RemoveField(
            model_name='item',
            name='instrument_image3',
        ),
        migrations.CreateModel(
            name='itemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='explore.item')),
            ],
        ),
    ]
