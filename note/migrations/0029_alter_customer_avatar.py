# Generated by Django 4.1.4 on 2023-10-06 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0028_alter_customer_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='avatar',
            field=models.ImageField(default='a3.jfif', null=True, upload_to='static/images'),
        ),
    ]
