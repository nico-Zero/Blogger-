# Generated by Django 4.1.13 on 2023-12-22 21:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_alter_profile_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(default="no_picture.png", upload_to="avatars"),
        ),
    ]