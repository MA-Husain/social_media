# Generated by Django 5.0.6 on 2024-06-19 20:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core_func", "0002_profile_first_name_profile_last_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="last_name",
        ),
    ]