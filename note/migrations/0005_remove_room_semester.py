# Generated by Django 4.2.3 on 2023-07-13 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_room_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='semester',
        ),
    ]