# Generated by Django 5.0.2 on 2024-02-09 04:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0028_remove_review_created_at_alter_review_comment_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='is_rated',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('item', 'user')},
        ),
    ]
