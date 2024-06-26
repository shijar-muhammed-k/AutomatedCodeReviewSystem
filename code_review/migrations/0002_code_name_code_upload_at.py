# Generated by Django 5.0.2 on 2024-03-16 05:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("code_review", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="code",
            name="name",
            field=models.CharField(default=2020, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="code",
            name="upload_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
