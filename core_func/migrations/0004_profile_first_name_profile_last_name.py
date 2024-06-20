# Generated by Django 5.0.6 on 2024-06-19 20:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core_func", "0003_remove_profile_first_name_remove_profile_last_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="first_name",
            field=models.CharField(default="DefaultFirstName", max_length=100),
        ),
        migrations.AddField(
            model_name="profile",
            name="last_name",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
