# Generated by Django 4.2.1 on 2023-05-05 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("friendships", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="friendship",
            name="from_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="friendship_sent",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="friendship",
            name="to_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="friendship_received",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
