# Generated by Django 5.0 on 2024-02-07 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guardian_app', '0002_remove_message_room_chat_message_chat_delete_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='uuid',
        ),
    ]