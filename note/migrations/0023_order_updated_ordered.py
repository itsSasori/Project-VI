# Generated by Django 4.2.3 on 2023-10-02 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0022_alter_order_date_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='updated_ordered',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
