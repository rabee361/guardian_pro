# Generated by Django 5.0 on 2024-02-16 08:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guardian_app', '0009_alter_test_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='date',
            field=models.DateField(default=datetime.date(2024, 2, 16)),
        ),
    ]
