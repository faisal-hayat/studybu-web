# Generated by Django 4.1 on 2022-10-07 15:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("base", "0002_topic_rooms_host_message_rooms_topic"),
    ]

    operations = [
        migrations.RenameModel(old_name="Rooms", new_name="Room",),
    ]